'''
This file extract the necessary information from 2018.csv to another output file.
The output csv file contains departure delay times each airline.
Input file: 2018.csv
Output file: delay_vs_airline_in2018.csv
'''

import pandas as pd

file='../../data/2018.csv'
data=pd.read_csv(file) #read file
flights=data.loc[data['CANCELLED']==0] #data excluding cancelled flights
airlines=set(data['OP_CARRIER']) #set of names of airlines

delay_vs_airline_in2018=pd.DataFrame(index=range(len(flights.index)),columns=airlines)
for name in airlines:
    delay_vs_airline_in2018[name]=flights.loc[flights['OP_CARRIER']==name]['DEP_DELAY']
delay_vs_airline_in2018.to_csv('delay_vs_airline_in2018.csv')
