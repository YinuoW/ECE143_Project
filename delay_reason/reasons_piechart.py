import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data_dir = "./data/2018.csv"
airline2018_dir = './data/airline2018_lookup.csv'

df_airline2018 = pd.read_csv(airline2018_dir)
df = pd.read_csv(data_dir)

labels = ['CARRIER_DELAY', 'WEATHER_DELAY', 'LATE_AIRCRAFT_DELAY', 'NAS_DELAY', 'SECURITY_DELAY']
# print(df.loc[df['LATE_AIRCRAFT_DELAY']>0][df['CANCELLED']==0])
# print(df.loc[df['CANCELLED']==1])
sizes = [df.loc[df['CARRIER_DELAY']>0].count()[0],
         df.loc[df['WEATHER_DELAY']>0].count()[0],
         df.loc[df['LATE_AIRCRAFT_DELAY']>0].count()[0],
         df.loc[df['NAS_DELAY']>0].count()[0],
         df.loc[df['SECURITY_DELAY']>0].count()[0]
        ]
# print(sizes) # adds up to 1433, which is the total number of participants
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'c']
qualitative_colors = sns.color_palette("BrBG", 4)
div_colors = sns.diverging_palette(10, 220, sep=80, n=4)
explode = (0.1, 0.1, 0.1, 0.1, 0.1)
fig1, ax1 = plt.subplots()
# theme = plt.get_cmap('bwr')
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', explode=explode, colors = qualitative_colors)
ax1.axis('equal')
ax1.set_title('Percentage of number of flights caused by each delay_reason')
plt.rcParams['font.size'] = 20
plt.show()

# ### percentage of delay time
# labels = ['CARRIER_DELAY', 'WEATHER_DELAY', 'LATE_AIRCRAFT_DELAY', 'NAS_DELAY', 'SECURITY_DELAY']
# # print(df['LATE_AIRCRAFT_DELAY'].sum())
# # print(df.loc[df['CANCELLED']==1])
# sizes = [df['CARRIER_DELAY'].sum(),
#          df['WEATHER_DELAY'].sum(),
#          df['LATE_AIRCRAFT_DELAY'].sum(),
#          df['NAS_DELAY'].sum(),
#          df['SECURITY_DELAY'].sum()
#         ]
# # print(sizes) # adds up to 1433, which is the total number of participants
# colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'c']
# qualitative_colors = sns.color_palette("Set2", 4)
# div_colors = sns.diverging_palette(10, 220, sep=80, n=4)
# div_colors2 = sns.diverging_palette(220, 20, n=4)
# yello_green = sns.color_palette("BrBG", 4)
# explode = (0.1, 0.1, 0.1, 0.1, 0.1)
# fig1, ax1 = plt.subplots()
# # theme = plt.get_cmap('bwr')
# ax1.pie(sizes, labels=labels, autopct='%1.1f%%', explode = explode, colors = yellow_green)
# ax1.axis('equal')
# ax1.set_title('Percentage of total delay time of each delay_reason')
# plt.show()