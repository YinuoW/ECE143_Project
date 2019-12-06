'''
This file extracts the delay rates for each of the airlinse 
and compiles them into a csv file for each airline.
'''

import pandas as pd

file='../../data/2018.csv'
flights=pd.read_csv(file) # all flights
un_flights=flights.loc[flights['CANCELLED']==0]
airlines=set(flights['OP_CARRIER']) # set of names of airlines

delay_freq=pd.DataFrame(index=airlines,columns=['delay','on-time_and_adv','total_flights'])
for name in airlines:
    delay_freq.loc[name]['delay']=un_flights.loc[un_flights['DEP_DELAY']>0].loc[un_flights['OP_CARRIER']==name].count()['FL_DATE']
    delay_freq.loc[name]['total_flights']=flights.loc[flights['OP_CARRIER']==name].count()['FL_DATE']
    delay_freq.loc[name]['on-time_and_adv']=delay_freq.loc[name]['total_flights']-delay_freq.loc[name]['delay']
    delay_freq.loc[name]=delay_freq.loc[name].div(delay_freq.loc[name]['total_flights'])
delay_freq=delay_freq.sort_values(by='on-time_and_adv')
delay_freq.to_csv('delay_rate.csv')
