import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# file='2018.csv'
# readlines=1000
# data=pd.read_csv(file) #read file
# flights=data.loc[data['CANCELLED']==0] #data excluding cancelled flights
# airlines=set(data['OP_CARRIER']) #set of names of airlines
#
# delay_vs_airline_in2018=pd.DataFrame(index=range(len(flights.index)),columns=airlines)
# for name in airlines:
#     delay_vs_airline_in2018[name]=flights.loc[flights['OP_CARRIER']==name]['DEP_DELAY']
# delay_vs_airline_in2018.to_csv('delay_vs_airline_in2018.csv')

file='delay_vs_airline_in2018.csv'
delay_vs_airline_in2018=pd.read_csv(file,usecols=['9E','YX','UA','MQ','DL','AA','OO','OH','WN','NK','B6'])

airlines=list(delay_vs_airline_in2018.columns)
airlines_name={'F9':'Frontier Airlines', '9E':'Endeavor Air', 'EV':'ExpressJet Airlines', 'YX':'Midwest Airlines', 'UA':'United Airlines', 'VX':'Virgin America', 'MQ':'Envoy Air',
               'DL':'Delta Air Lines', 'AA':'American Airlines', 'OO':'SkyWest Airlines', 'YV':'Mesa Airlines', 'HA':'Hawaiian Airlines',
               'AS':'Alaska Airlines', 'OH':'PSA Airlines', 'G4':'Allegiant Air', 'WN':'Southwest Airlines', 'NK':'Spirit Airlines', 'B6':'JetBlue Airways'}
delay_vs_airline_in2018=delay_vs_airline_in2018.rename(columns=airlines_name)
delay_vs_airline_in2018.boxplot(sym='',vert=False,showmeans=True,manage_ticks=True)


plt.xlabel('Average delay')
plt.ylabel('Airlines')
plt.title('Average delay vs airlines')
plt.show()
