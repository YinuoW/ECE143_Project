import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

'''
This file plots the flight counts for each airline.
'''

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
    count.append(c)

count = [916818,245917,949283,305010,202890,83723,296001,278457,774137,176178,1352552,215138,316090,245761,96221,621565,120035,17670]
sns.countplot(df4['OP_CARRIER'], palette="Set2")
plt.xticks(rotation=90)
plt.title('Number of Flights of Airlines')
plt.show()
