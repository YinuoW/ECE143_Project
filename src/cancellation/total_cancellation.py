# cancellation rate of each airline with color bar
import pandas as pd
import plotly.graph_objs as go
from plotly.offline import iplot

data_dir = "../../data/2018.csv"
airline2018_dir = '../../data/airline2018_lookup.csv'
df_airline2018 = pd.read_csv(airline2018_dir)
df = pd.read_csv(data_dir)

airlines_code = list(df_airline2018['Code'])
airlines_name = list(df_airline2018['Description'])

code_name = dict()
for idx, air in enumerate(airlines_code):
    code_name[air] = airlines_name[idx]

df4 = df.loc[:,['OP_CARRIER']]
df4['OP_CARRIER'] = df4['OP_CARRIER'].replace(code_name)
count = []
op_list = df4['OP_CARRIER'].unique()
for op in op_list:
    c = df4.loc[df4['OP_CARRIER'] == op].count()
    count.append(c[0])

name_count_dict = dict()
op_list = df4['OP_CARRIER'].unique()
for idx, op in enumerate(op_list):
    name_count_dict[op] = count[idx]


name_count_dict_value = list(name_count_dict.values())
name_count_dict_value.sort(reverse=True)
name_count_dict_key = list(name_count_dict.keys())
new_key = list()
for i in name_count_dict_value:
    for key in name_count_dict.keys():
        if name_count_dict[key] == i:
            new_key.append(key)

name_count_dict_ordered = dict()
for idx, op in enumerate(new_key):
    name_count_dict_ordered[op] = name_count_dict_value[idx]

keylist = list(name_count_dict_ordered.keys())
valuelist = list(name_count_dict_ordered.values())
df_ = pd.DataFrame({'Airlines': keylist[0:10], 'Number of Flights' : valuelist[0:10]})
df_[['Airlines','Number of Flights']]

#### Total cancellation
cancel_group = df.groupby(['OP_CARRIER'])['CANCELLED'].sum().sort_values(ascending=False)
cancel_group = cancel_group.reset_index()
cancel_group['OP_CARRIER'] = cancel_group['OP_CARRIER'].replace(code_name)

drop_list = list()
for idx, i in enumerate(cancel_group['OP_CARRIER']):
    if i not in keylist[0:10]:
        drop_list.append(idx)
cancel_group = cancel_group.drop(drop_list)
cancel_group_new = pd.DataFrame(list(cancel_group['CANCELLED']),index=cancel_group['OP_CARRIER'], columns = {'Cancelled'})
df_new = pd.DataFrame(list(df_['Number of Flights']), index = df_['Airlines'], columns = {'Numbers'})
cancell_count_airlines = pd.concat([cancel_group_new, df_new], axis=1, join='inner')
print(cancell_count_airlines)


layout = go.Layout(title='Cancelled Flights vs. Total Flights',
                    xaxis={'title':'Airlines'},
                    yaxis={'title':'Number of Flights'})

fig = go.Figure(data=[
    go.Bar(name='Cancelled flights', x=cancel_group['OP_CARRIER'], y=cancell_count_airlines['Cancelled']),
    go.Bar(name='Total flights', x=cancel_group['OP_CARRIER'], y=cancell_count_airlines['Numbers'])
], layout = layout)
# Change the bar mode

fig.update_layout(barmode='group')
fig.show()