import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

start=time.perf_counter()

file='2018.csv'
readlines=80
flights=pd.read_csv(file,nrows=readlines) # all flights
flights=flights.loc[flights['CANCELLED']==0]
airlines=set(flights['OP_CARRIER']) # set of names of airlines

# define dataframes
time_block=pd.DataFrame(index=['morning','afternoon','night'],columns=['avg_dep_delay'])
tmp=flights.groupby('DEP_TIME_BLK')['DEP_DELAY'].sum()
ref={'0001-0559':'night','0600-0659':'morning', '0700-0759':'morning', '0800-0859':'morning',
     '0900-0959':'morning','1000-1059':'morning', '1100-1159':'morning','1200-1259':'afternoon', '1300-1359':'afternoon', '1400-1459':'afternoon',
       '1500-1559':'afternoon', '1600-1659':'afternoon', '1700-1759':'afternoon','1800-1859':'night', '1900-1959':'night',
       '2000-2059':'night', '2100-2159':'night', '2200-2259':'night', '2300-2359':'night'}
for i in time_block.index:
    time_block.loc[i]=0
for i in tmp.index:
    time_block.loc[ref[i]]+=tmp[i]
counts={'morning':0,'afternoon':0,'night':0}
for i in ref.keys():
    counts[ref[i]]+=list(flights['DEP_TIME_BLK']).count(i)
for i in time_block.index:
    time_block.loc[i]['avg_dep_delay']=time_block.loc[i]['avg_dep_delay']/counts[i]
width=0.4
p1=plt.bar(time_block.index,time_block['avg_dep_delay'],width)
plt.legend(['Average departure delay'],loc='best')
plt.show()
