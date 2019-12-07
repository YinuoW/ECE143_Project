'''
This file extracts the data from all flights in 2018 to form a csv file that contains 
all the time blocks for delays of each airline.
'''
import pandas as pd

file='../../data/2018.csv'
flights=pd.read_csv(file) # all flights
flights=flights.loc[flights['CANCELLED']==0]
airlines=set(flights['OP_CARRIER']) # set of names of airlines

# define dataframes
time_block=pd.DataFrame(columns=['morning','afternoon','night'],index=airlines)
ref={'0001-0559':'night','0600-0659':'morning', '0700-0759':'morning', '0800-0859':'morning',
         '0900-0959':'morning','1000-1059':'morning', '1100-1159':'morning','1200-1259':'afternoon', '1300-1359':'afternoon', '1400-1459':'afternoon',
           '1500-1559':'afternoon', '1600-1659':'afternoon', '1700-1759':'afternoon','1800-1859':'night', '1900-1959':'night',
           '2000-2059':'night', '2100-2159':'night', '2200-2259':'night', '2300-2359':'night'}
for i in time_block.index:
    time_block.loc[i] = 0
for name in airlines:
    tmp=flights.loc[flights['OP_CARRIER']==name].groupby('DEP_TIME_BLK')['DEP_DELAY'].sum()
    for i in tmp.index:
        time_block.loc[name][ref[i]]+=tmp[i]
    counts={'morning':0,'afternoon':0,'night':0}
    for i in ref.keys():
        counts[ref[i]]+=list(flights.loc[flights['OP_CARRIER']==name]['DEP_TIME_BLK']).count(i)
    for i in time_block.columns:
        time_block.loc[name][i]=time_block.loc[name][i]/counts[i]
print('time_block.csv')
time_block.to_csv('time_block.csv')
