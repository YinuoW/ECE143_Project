# This file extract the dataframe for drawing the scoring plots

import pandas as pd

file='../../data/2018.csv'
flights=pd.read_csv(file) #read file
uncancelled_flights=flights.loc[flights['CANCELLED']==0] #data excluding cancelled flights
airlines=set(flights['OP_CARRIER']) #set of names of airlines

airlines_stats=pd.DataFrame(index=airlines,columns=['dep_delay','arr_delay','cancel_times'])
for name in airlines:
    airlines_stats.loc[name]['dep_delay']= uncancelled_flights.loc[uncancelled_flights['OP_CARRIER']==name]['DEP_DELAY'].mean()
    airlines_stats.loc[name]['arr_delay'] = uncancelled_flights.loc[uncancelled_flights['OP_CARRIER'] == name]['ARR_DELAY'].mean()
    airlines_stats.loc[name]['cancel_times'] = list(flights.loc[flights['OP_CARRIER'] == name]['CANCELLED']).count(1)
airlines_stats.to_csv('airlines_stats.csv')