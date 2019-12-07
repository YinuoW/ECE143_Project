'''
This file plots the delay of each flight by time.
Each flight departure is delayed by either less than or more than 15 mins.
Input file: 2018.csv
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

start=time.perf_counter()

file='../../data/2018.csv'
flights=pd.read_csv(file) # all flights
airlines=set(flights['OP_CARRIER']) # set of names of airlines

# define dataframes
# frequency_dep_delay_<15_and_>15_vs_airline, cancelled filghts count as >15 min
frequency_dep_delay_vs_airline=pd.DataFrame(index=airlines,columns=['dep_delay>15_num','dep_delay<15_num','total_flight_num','<15_freq','>15_freq'])

# compute dataframes
for name in airlines:
    frequency_dep_delay_vs_airline.loc[name,'total_flight_num']=list(flights['OP_CARRIER']).count(name)
    frequency_dep_delay_vs_airline.loc[name,'dep_delay<15_num']=list(flights.loc[flights['OP_CARRIER']==name,'DEP_DEL15']).count(0)
    frequency_dep_delay_vs_airline.loc[name,'dep_delay>15_num']=frequency_dep_delay_vs_airline.loc[name,'total_flight_num']-frequency_dep_delay_vs_airline.loc[name,'dep_delay<15_num']
    frequency_dep_delay_vs_airline.loc[name,'<15_freq']=frequency_dep_delay_vs_airline.loc[name,'dep_delay<15_num']/frequency_dep_delay_vs_airline.loc[name,'total_flight_num']
    frequency_dep_delay_vs_airline.loc[name,'>15_freq']=frequency_dep_delay_vs_airline.loc[name,'dep_delay>15_num']/frequency_dep_delay_vs_airline.loc[name,'total_flight_num']

# visualization
# plot frequency_dep_delay_<15_and_>15_vs_airline, cancelled filghts count as >15 min
width=0.4
frequency_dep_delay_vs_airline=frequency_dep_delay_vs_airline.sort_values(by='<15_freq')
p1 = plt.bar(frequency_dep_delay_vs_airline.index,frequency_dep_delay_vs_airline['<15_freq'],width)
p2 = plt.bar(frequency_dep_delay_vs_airline.index,frequency_dep_delay_vs_airline['>15_freq'],width,bottom=frequency_dep_delay_vs_airline['<15_freq'])
plt.yticks(np.arange(0, 1.1, 0.1))
plt.legend((p1[0], p2[0]), ('Depart-delay <15 min rate', 'Depart-delay >15 min rate'),loc='lower right')

#show plots
plt.show()

end=time.perf_counter()
print('Time used:',end-start)
