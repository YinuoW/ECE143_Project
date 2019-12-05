import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import re

data_dir = "../../data/2018.csv"
airline2018_dir = '../../data/airline2018_lookup.csv'


df_airline2018 = pd.read_csv(airline2018_dir)
df = pd.read_csv(data_dir,usecols=['OP_CARRIER','ARR_DELAY'])

airlines_code = list(df_airline2018['Code'])
airlines_name = list(df_airline2018['Description'])


to_drop= ['AS','EV','F9','G4','HA','NK','VX','YV']
df = df[~df['OP_CARRIER'].isin(to_drop)]

# remove all words within brackets

airlines_name = [re.sub("[\(\[].*?[\)\]]", "", elem) for elem in airlines_name]

code_name = dict()
for idx, air in enumerate(airlines_code):
    code_name[air] = airlines_name[idx]

airline_name_2018 = list()
for air in set(df['OP_CARRIER']):
    airline_name_2018.append(code_name[air])

df3 = df.loc[:, ['OP_CARRIER', 'ARR_DELAY']]
df3['OP_CARRIER'] = df3['OP_CARRIER'].replace(code_name)
qualitative_colors = sns.color_palette("Set3", 18)
ax = sns.stripplot(y="OP_CARRIER", x="ARR_DELAY", data=df3, jitter=True,linewidth=0.2, palette = qualitative_colors)
ax.set_xticklabels(['{:2.0f}h{:2.0f}m'.format(*[int(y) for y in divmod(x,60)])
                          for x in ax.get_xticks()])
ax.set_title('Arrival Delay Distribution of Airlines')
plt.show()