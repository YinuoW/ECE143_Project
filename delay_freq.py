import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

start=time.perf_counter()

file='2018.csv'
readlines=8000
flights=pd.read_csv(file,nrows=readlines) # all flights
un_flights=flights.loc[flights['CANCELLED']==0]
airlines=set(flights['OP_CARRIER']) # set of names of airlines

delay_freq=pd.DataFrame(index=airlines,columns=['delay','on-time_and_adv','total_flights'])
for name in airlines:
    delay_freq.loc[name]['delay']=un_flights.loc[un_flights['DEP_DELAY']>0].loc[un_flights['OP_CARRIER']==name].count()['FL_DATE']
    delay_freq.loc[name]['total_flights']=flights.loc[flights['OP_CARRIER']==name].count()['FL_DATE']
    delay_freq.loc[name]['on-time_and_adv']=delay_freq.loc[name]['total_flights']-delay_freq.loc[name]['delay']
    delay_freq.loc[name]=delay_freq.loc[name].div(delay_freq.loc[name]['total_flights'])
print(delay_freq)
delay_freq=delay_freq.sort_values(by='on-time_and_adv')
# visualization
width=0.4
p1 = plt.bar(delay_freq.index,delay_freq['delay'],width)
p2 = plt.bar(delay_freq.index,delay_freq['on-time_and_adv'],width,bottom=delay_freq['delay'])
plt.yticks(np.arange(0, 1.1, 0.1))
plt.legend((p1[0], p2[0]), ('Delay rate','On-time and advance rate'),loc='best')
plt.show()