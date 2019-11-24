import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# file='2018.csv'
# readlines=2000
# flights=pd.read_csv(file) # all flights
# flights=flights.loc[flights['CANCELLED']==0]
# airlines=set(flights['OP_CARRIER']) # set of names of airlines
#
# # define dataframes
# time_block=pd.DataFrame(columns=['morning','afternoon','night'],index=airlines)
# ref={'0001-0559':'night','0600-0659':'morning', '0700-0759':'morning', '0800-0859':'morning',
#          '0900-0959':'morning','1000-1059':'morning', '1100-1159':'morning','1200-1259':'afternoon', '1300-1359':'afternoon', '1400-1459':'afternoon',
#            '1500-1559':'afternoon', '1600-1659':'afternoon', '1700-1759':'afternoon','1800-1859':'night', '1900-1959':'night',
#            '2000-2059':'night', '2100-2159':'night', '2200-2259':'night', '2300-2359':'night'}
# for i in time_block.index:
#     time_block.loc[i] = 0
# for name in airlines:
#     tmp=flights.loc[flights['OP_CARRIER']==name].groupby('DEP_TIME_BLK')['DEP_DELAY'].sum()
#     for i in tmp.index:
#         time_block.loc[name][ref[i]]+=tmp[i]
#     counts={'morning':0,'afternoon':0,'night':0}
#     for i in ref.keys():
#         counts[ref[i]]+=list(flights.loc[flights['OP_CARRIER']==name]['DEP_TIME_BLK']).count(i)
#     for i in time_block.columns:
#         time_block.loc[name][i]=time_block.loc[name][i]/counts[i]
# time_block.to_csv('time_block.csv')
file='time_block.csv'
time_block=pd.read_csv(file,index_col=0,header=0)
airlines=list(time_block.index)
airlines_name={'F9':'Frontier Airlines', '9E':'Endeavor Air', 'EV':'ExpressJet Airlines', 'YX':'Midwest Airlines', 'UA':'United Airlines', 'VX':'Virgin America', 'MQ':'Envoy Air',
               'DL':'Delta Air Lines', 'AA':'American Airlines', 'OO':'SkyWest Airlines', 'YV':'Mesa Airlines', 'HA':'Hawaiian Airlines',
               'AS':'Alaska Airlines', 'OH':'PSA Airlines', 'G4':'Allegiant Air', 'WN':'Southwest Airlines', 'NK':'Spirit Airlines', 'B6':'JetBlue Airways'}
time_block=time_block.rename(index=airlines_name)
airlines=list(time_block.index)
print(time_block)
width=0.2
# x = np.arange(len(airlines))
# fig, ax = plt.subplots()
# rects1 = ax.bar(x-width,time_block['morning'], width, label='Average delay from 6am to 12pm')
# rects2 = ax.bar(x,time_block['afternoon'], width, label='Average delay from 12pm to 6pm')
# rects3 = ax.bar(x + width,time_block['night'], width, label='Average delay from 6pm to 6am')
# ax.set_ylabel('Average delay')
# ax.set_title('Average delay time block')
# ax.set_xticks(x)
# ax.set_xticklabels(airlines)
# ax.legend()
x=np.arange(len(airlines))
p1=plt.barh(x,time_block['morning'],fill=False,edgecolor='darkred',lw=2)
p2=plt.barh(x,time_block['afternoon'],fill=False,edgecolor='navy',lw=2)
p3=plt.barh(x,time_block['night'],fill=False,edgecolor='darkgreen',lw=2)
plt.yticks(x,airlines)
# for i,j in zip(time_block['morning'],x):
#     plt.text(i+1,j, '%.2f' % i, ha='center', va='bottom',rotation=-90,)
# for i,j in zip(time_block['afternoon'],x):
#     plt.text(i+1,j, '%.2f' % i, ha='center', va='bottom',rotation=-90)
# for i,j in zip(time_block['night'],x):
#     plt.text(i+1,j, '%.2f' % i, ha='center', va='bottom',rotation=-90)
plt.legend((p1[0], p2[0],p3[0]), ('6am to 12pm','12pm to 6 pm','6pm to 6am'),loc='best')
plt.xlabel('Average delay')
plt.title('Average delay time block')

plt.show()
