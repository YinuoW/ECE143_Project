#### Total cancellation
import pandas as pd
import plotly.graph_objs as go

data_dir = "../data/2018.csv"
airline2018_dir = '../data/airline2018_lookup.csv'
df_airline2018 = pd.read_csv(airline2018_dir)
df = pd.read_csv(data_dir)

airlines_code = list(df_airline2018['Code'])
airlines_name = list(df_airline2018['Description'])

code_name = dict()
for idx, air in enumerate(airlines_code):
    code_name[air] = airlines_name[idx]

cancel_group = df.groupby(['OP_CARRIER'])['CANCELLED'].sum().sort_values(ascending=False)
cancel_group = cancel_group.reset_index()
cancel_group['OP_CARRIER'] = cancel_group['OP_CARRIER'].replace(code_name)

keylist = ['Southwest Airlines Co.', 'JetBlue Airways', 'Endeavor Air Inc.', 'PSA Airlines Inc.', 'United Air Lines Inc.', 'Mesa Airlines Inc.', 'ExpressJet Airlines Inc.', 'Envoy Air', 'Spirit Air Lines', 'Alaska Airlines Inc.', 'Republic Airline', 'American Airlines Inc.', 'Allegiant Air', 'SkyWest Airlines Inc.', 'Delta Air Lines Inc.', 'Frontier Airlines Inc.', 'Hawaiian Airlines Inc.', 'Virgin America']
valuelist = [1352552, 949283, 916818, 774137, 621565, 316090, 305010, 296001, 278457, 245917, 245761, 215138, 202890, 176178, 120035, 96221, 83723, 17670]
df_ = pd.DataFrame({'Airlines': keylist[0:10], 'Number of Flights' : valuelist[0:10]})
df_[['Airlines','Number of Flights']]

drop_list = list()
for idx, i in enumerate(cancel_group['OP_CARRIER']):
    if i not in keylist[0:10]:
        drop_list.append(idx)
cancel_group = cancel_group.drop(drop_list)
cancel_group_new = pd.DataFrame(list(cancel_group['CANCELLED']),index=cancel_group['OP_CARRIER'], columns = {'Cancelled'})
df_new = pd.DataFrame(list(df_['Number of Flights']), index = df_['Airlines'], columns = {'Numbers'})
cancell_count_airlines = pd.concat([cancel_group_new, df_new], axis=1, join='inner')

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
