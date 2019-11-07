import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import calendar
start=time.perf_counter()

file='2018.csv'
readlines=800000
flights=pd.read_csv(file,nrows=readlines) # all flights
airlines=set(flights['OP_CARRIER']) # set of names of airlines
months=list(calendar.month_name)[1:] # list of month names
uncancelled_flights=flights.loc[flights['CANCELLED']==0] # excluding cancelled flights
uncancelled_flights_date_index=uncancelled_flights.set_index('FL_DATE').sort_index()

# define dataframes
# frequency_dep_delay_<15_and_>15_vs_airline, cancelled filghts count as >15 min
frequency_dep_delay_vs_airline=pd.DataFrame(index=airlines,columns=['dep_delay>15_num','dep_delay<15_num','total_flight_num','<15_freq','>15_freq'])
# airlines vs average delay in 2018
airlines_vs_dep_delay=pd.DataFrame(index=airlines,columns=['Average depart-delay'])
# airline delay vs date
airlines_delay_vs_month=pd.DataFrame(index=airlines,columns=list(range(1,13)))

# compute dataframes
for name in airlines:
    # frequency_dep_delay_vs_airline.loc[name,'total_flight_num']=list(flights['OP_CARRIER']).count(name)
    # frequency_dep_delay_vs_airline.loc[name,'dep_delay<15_num']=list(flights.loc[flights['OP_CARRIER']==name,'DEP_DEL15']).count(0)
    # frequency_dep_delay_vs_airline.loc[name,'dep_delay>15_num']=frequency_dep_delay_vs_airline.loc[name,'total_flight_num']-frequency_dep_delay_vs_airline.loc[name,'dep_delay<15_num']
    # frequency_dep_delay_vs_airline.loc[name,'<15_freq']=frequency_dep_delay_vs_airline.loc[name,'dep_delay<15_num']/frequency_dep_delay_vs_airline.loc[name,'total_flight_num']
    # frequency_dep_delay_vs_airline.loc[name,'>15_freq']=frequency_dep_delay_vs_airline.loc[name,'dep_delay>15_num']/frequency_dep_delay_vs_airline.loc[name,'total_flight_num']
    # airlines_vs_dep_delay.loc[name,'Average depart-delay']=uncancelled_flights.loc[uncancelled_flights['OP_CARRIER']==name,'DEP_DELAY'].mean()
    for i in range(1,13):
        if i==1 or 3 or 5 or 7 or 8:
            airlines_delay_vs_month.loc[name,i]=uncancelled_flights_date_index.loc['2018-0'+str(i)+'-01':'2018-0'+str(i)+'-31'].loc[uncancelled_flights_date_index['OP_CARRIER']==name]['DEP_DELAY'].mean()
        if i==10 or 12:
            airlines_delay_vs_month.loc[name,i]=uncancelled_flights_date_index.loc['2018-'+str(i)+'-01':'2018-'+str(i)+'-31'].loc[uncancelled_flights_date_index['OP_CARRIER']==name]['DEP_DELAY'].mean()
        if i == 4 or 6 or 9:
            airlines_delay_vs_month.loc[name, i] = uncancelled_flights_date_index.loc['2018-0' + str(i) + '-01':'2018-0' + str(i) + '-30'].loc[uncancelled_flights_date_index['OP_CARRIER']==name]['DEP_DELAY'].mean()
        if i == 11:
            airlines_delay_vs_month.loc[name, i] = uncancelled_flights_date_index.loc['2018-' + str(i) + '-01':'2018-' + str(i) + '-30'].loc[uncancelled_flights_date_index['OP_CARRIER']==name]['DEP_DELAY'].mean()
        if i == 2:
            airlines_delay_vs_month.loc[name, i] = uncancelled_flights_date_index.loc['2018-02-01':'2018-02-28'].loc[uncancelled_flights_date_index['OP_CARRIER']==name]['DEP_DELAY'].mean()
print(airlines_delay_vs_month)
# # visualization
# # plot frequency_dep_delay_<15_and_>15_vs_airline, cancelled filghts count as >15 min
# width=0.4
# frequency_dep_delay_vs_airline=frequency_dep_delay_vs_airline.sort_values(by='<15_freq')
# p1 = plt.bar(frequency_dep_delay_vs_airline.index,frequency_dep_delay_vs_airline['<15_freq'],width)
# p2 = plt.bar(frequency_dep_delay_vs_airline.index,frequency_dep_delay_vs_airline['>15_freq'],width,bottom=frequency_dep_delay_vs_airline['<15_freq'])
# plt.yticks(np.arange(0, 1.1, 0.1))
# plt.legend((p1[0], p2[0]), ('Depart-delay <15 min rate', 'Depart-delay >15 min rate'),loc='lower right')
# # plot airlines vs delay
# airlines_vs_dep_delay.sort_values(by='Average depart-delay').plot(kind='bar')
#
# #show plots
# plt.show()

end=time.perf_counter()
print('Time used:',end-start)