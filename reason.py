import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

start=time.perf_counter()

file='2018.csv'
readlines=80000
flights=pd.read_csv(file,nrows=readlines) # all flights
flights=flights.loc[flights['CANCELLED']==0]
airlines=set(flights['OP_CARRIER']) # set of names of airlines

# define dataframes
# frequency_dep_delay_<15_and_>15_vs_airline, cancelled filghts count as >15 min
reasons_vs_airline=pd.DataFrame(index=airlines,columns=['CARRIER_DELAY','WEATHER_DELAY','SECURITY_DELAY','LATE_AIRCRAFT_DELAY'])
for name in airlines:
    reasons_vs_airline.loc[name]=0
for name in airlines:
    reasons_vs_airline.loc[name]['total_flights'] = flights.loc[flights['OP_CARRIER'] == name].count()['FL_DATE']
    for reason in list(reasons_vs_airline.columns)[:-1]:
        reasons_vs_airline.loc[name][reason]=flights.loc[flights['OP_CARRIER']==name].count()[reason]-list(flights.loc[flights['OP_CARRIER']==name][reason]).count(0)
    reasons_vs_airline.loc[name]=reasons_vs_airline.loc[name].div(reasons_vs_airline.loc[name].sum())
print(reasons_vs_airline)

# visualization
width=0.4
p1 = plt.bar(reasons_vs_airline.index,reasons_vs_airline['CARRIER_DELAY'],width)
p2 = plt.bar(reasons_vs_airline.index,reasons_vs_airline['WEATHER_DELAY'],width,bottom=reasons_vs_airline['CARRIER_DELAY'])
p3 = plt.bar(reasons_vs_airline.index,reasons_vs_airline['SECURITY_DELAY'],width,bottom=reasons_vs_airline['WEATHER_DELAY'])
p4 = plt.bar(reasons_vs_airline.index,reasons_vs_airline['LATE_AIRCRAFT_DELAY'],width,bottom=reasons_vs_airline['SECURITY_DELAY'])
plt.yticks(np.arange(0, 1.1, 0.1))
plt.legend((p1[0], p2[0],p3[0],p4[0]), ('CARRIER_DELAY','WEATHER_DELAY','SECURITY_DELAY','LATE_AIRCRAFT_DELAY'),loc='best')
plt.show()