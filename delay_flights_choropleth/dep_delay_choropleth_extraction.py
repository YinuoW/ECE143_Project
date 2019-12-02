'''
This file extracts the data for
the distribution of delay flights and total flights according to states
'''

import pandas as pd

file='../data/2018.csv'
readlines=10000
flights=pd.read_csv(file) # all flights
flights=flights.loc[flights['CANCELLED']==0]
states=set(flights['ORIGIN_STATE_ABR'])

states_stats=pd.DataFrame(index=states,columns=['dep_delay','arr_delay','total_flights'])
for state in states:
    states_stats.loc[state]['dep_delay']=flights.loc[flights['ORIGIN_STATE_ABR']==state]['DEP_DELAY'].mean()
    states_stats.loc[state]['arr_delay'] = flights.loc[flights['ORIGIN_STATE_ABR'] == state]['ARR_DELAY'].mean()
    states_stats.loc[state]['total_flights'] = list(flights['ORIGIN_STATE_ABR']).count(state)
states_stats['state']=states_stats.index
states_stats.to_csv('states_stats.csv')