import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

data_dir = "./data/2018.csv"
airline2018_dir = './data/airline2018_lookup.csv'

df_airline2018 = pd.read_csv(airline2018_dir)
df = pd.read_csv(data_dir)

airlines_code = list(df_airline2018['Code'])
airlines_name = list(df_airline2018['Description'])

code_name = dict()
for idx, air in enumerate(airlines_code):
    code_name[air] = airlines_name[idx]

airline_name_2018 = list()
for air in set(df['OP_CARRIER']):
    airline_name_2018.append(code_name[air])

df2 = df.loc[:, ['OP_CARRIER', 'DEP_DELAY']]
df2['OP_CARRIER'] = df2['OP_CARRIER'].replace(code_name)

qualitative_colors = sns.color_palette("Set3", 18)
ax = sns.stripplot(y="OP_CARRIER", x="DEP_DELAY", data=df2, jitter=True, linewidth=0.2, palette = qualitative_colors)
ax.set_xticklabels(['{:2.0f}h{:2.0f}m'.format(*[int(y) for y in divmod(x,60)]) for x in ax.get_xticks()])
ax.set_title('Departure Delay Distribution of Airlines')
plt.show()


# df3 = df.loc[:, ['OP_CARRIER', 'ARR_DELAY']]
# df3['OP_CARRIER'] = df3['OP_CARRIER'].replace(code_name)
# qualitative_colors = sns.color_palette("Set3", 18)
# ax = sns.stripplot(y="OP_CARRIER", x="ARR_DELAY", data=df3, jitter=True,linewidth=0.2, palette = qualitative_colors)
# ax.set_xticklabels(['{:2.0f}h{:2.0f}m'.format(*[int(y) for y in divmod(x,60)])
#                          for x in ax.get_xticks()])
# ax.set_title('Arrival Delay Distribution of Airlines')
# plt.show()