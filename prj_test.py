import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file='2018.csv'
data=pd.read_csv(file) #read file
uncancelled_flights=data.loc[data['CANCELLED']==0] #data excluding cancelled flights
airlines=set(data['OP_CARRIER']) #set of names of airlines

# define dataframes
# airlines vs delay
airlines_vs_depdelay=pd.DataFrame(index=['Average Delay'],columns=airlines)
# airline delay vs date
airlines_delay_vs_date=pd.DataFrame(columns=[])
# total cancelled times vs airlines
cancelled_vs_airlines=pd.DataFrame(index=['Cancellation times'],columns=airlines)
#distance vs delay
dist_vs_delay=pd.DataFrame(columns=[])

# compute dataframes
dist_vs_delay['DISTANCE']=uncancelled_flights['DISTANCE']
dist_vs_delay['DEP_DELAY']=uncancelled_flights['DEP_DELAY']

for name in airlines:
    airlines_vs_depdelay[name]=uncancelled_flights.loc[uncancelled_flights['OP_CARRIER']==name]['DEP_DELAY'].mean()
    airlines_delay_vs_date[name] = uncancelled_flights.loc[data['OP_CARRIER'] == name].groupby('FL_DATE')['DEP_DELAY'].mean()
    cancelled_vs_airlines[name] = data.loc[data['OP_CARRIER'] == name]['CANCELLED'].sum()

# visualization
# plot airlines vs delay
airlines_vs_depdelay.T.sort_values(by='Average Delay').plot(kind='bar')
plt.xticks(rotation=0)
# plot airline delay vs date
airlines_delay_vs_date[['UA','AS']].plot(kind='line') #using UA and AS as examples
plt.legend(loc='upper left')
plt.xlabel('Flight Date')
plt.ylabel('Average Delay')
plt.xticks(rotation=60)
# plot total cancelled times vs airlines
cancelled_vs_airlines.T.sort_values(by='Cancellation times').plot(kind='bar')
plt.xticks(rotation=0)
plt.legend(loc='upper left')
# plot dist vs delay
dist_vs_delay.plot.scatter(x='DISTANCE',y='DEP_DELAY')

#show plots
plt.show()