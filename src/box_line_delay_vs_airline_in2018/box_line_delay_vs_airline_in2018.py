'''
This file creates the box plot of departure delays for each airline.
Input file: delay_vs_airline_in2018.csv
'''

import pandas as pd
import matplotlib.pyplot as plt

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
