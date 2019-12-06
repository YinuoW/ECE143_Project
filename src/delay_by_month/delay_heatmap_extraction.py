'''
This file extracts the total delay times from all 2018 flights
and compiles them into a csv file for each airline according to months.
This allows easier generation of the heat map.
'''


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

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

month_dict = dict()
month_31=[1,3,5,7,8,10,12]
month_30=[4,6,9,11]
for i in range(1, 13):
    day_list = list()
    if i==2:
        for j in range(1,29):
            d = datetime.date(2018, i, j)
            day_list.append(str(d))
    if i in month_30:
        for j in range(1,31):
            d = datetime.date(2018, i, j)
            day_list.append(str(d))
    if i in month_31:
        for j in range(1,32):
            d = datetime.date(2018, i, j)
            day_list.append(str(d))
    month_dict[i] = day_list

month_name = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
df_drop_code_list = ['AS', 'YV', 'EV', 'NK', 'F9', 'G4', 'HA', 'VX']

idx = list()
for i in df_drop_code_list:
    df = df.drop(df[df['OP_CARRIER'] == i].index)

df['OP_CARRIER'] = df['OP_CARRIER'].replace(code_name)

df_day_delay = df[df['ARR_DELAY']>0]
df_day_delay = df_day_delay.groupby(['FL_DATE'])['ARR_DELAY'].count().sort_values(ascending=False)

monthly_delay = dict()
for i in month_dict:
    monthly_delay[i] = 0
    for d in month_dict[i]:
        monthly_delay[i] += df_day_delay[d]

df_day_delaytime_airline = df[df['ARR_DELAY']>0]
df_day_delaytime_airline = df_day_delaytime_airline[['ARR_DELAY','OP_CARRIER','FL_DATE']]
df_month_delaytime_airline = pd.DataFrame(columns=keylist[0:10], index=month_name)

for op in keylist[0:10]:
    monthly_delay = dict()
    df_op = df_day_delaytime_airline[df_day_delaytime_airline['OP_CARRIER'] == op]
    for i in month_dict:
        monthly_delay[i] = 0
        for d in month_dict[i]:
            monthly_delay[i] += df_op[df_op['FL_DATE'] == d]['ARR_DELAY'].sum()

    df_month_delaytime_airline[op] = list(monthly_delay.values())

df1_transposed = df_month_delaytime_airline.T
df1_transposed.to_csv('delay_heatmap.csv')
