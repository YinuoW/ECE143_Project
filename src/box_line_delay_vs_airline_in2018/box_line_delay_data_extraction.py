'''
This file produces the csv.file of airline delay time for all flights in 2018.
output csv: delay_vs_airline_in2018.csv
Output file is used to form boxplot in box_line_delay_data_extraction.py
'''

import pandas as pd

file='../../data/2018.csv'
data=pd.read_csv(file) #read file
flights=data.loc[data['CANCELLED']==0] #data excluding cancelled flights
airlines=set(data['OP_CARRIER']) #set of names of airlines

delay_vs_airline_in2018=pd.DataFrame(index=range(len(flights.index)),columns=airlines)
for name in airlines:
    delay_vs_airline_in2018[name]=flights.loc[flights['OP_CARRIER']==name]['DEP_DELAY']
print('delay_vs_airline_in2018.csv')
delay_vs_airline_in2018.to_csv('delay_vs_airline_in2018.csv')
