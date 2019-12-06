'''
This file extracts the necessary data from the 2018.csv for easier compilation of images.
The data extracted is the count for each of the reasons for delay, and is done for each airline.
File output: reasons_vs_airline.csv
'''

import pandas as pd

file='../../data/2018.csv'
flights=pd.read_csv(file) # all flights
flights=flights.loc[flights['CANCELLED']==0]
airlines=set(flights['OP_CARRIER']) # set of names of airlines

# define dataframes
reasons_vs_airline=pd.DataFrame(index=airlines,columns=['CARRIER_DELAY','WEATHER_DELAY','SECURITY_DELAY','LATE_AIRCRAFT_DELAY'])
for name in airlines:
    reasons_vs_airline.loc[name]=0
for name in airlines:
    reasons_vs_airline.loc[name]['total_flights'] = flights.loc[flights['OP_CARRIER'] == name].count()['FL_DATE']
    for delay_reason in list(reasons_vs_airline.columns)[:-1]:
        reasons_vs_airline.loc[name][delay_reason]=flights.loc[flights['OP_CARRIER']==name].count()[delay_reason]-list(flights.loc[flights['OP_CARRIER']==name][delay_reason]).count(0)
    reasons_vs_airline.loc[name]=reasons_vs_airline.loc[name].div(reasons_vs_airline.loc[name].sum())
reasons_vs_airline.sort_values(by='CARRIER_DELAY')
reasons_vs_airline.to_csv('reasons_vs_airline.csv')
