import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time


# file='2018.csv'
# flights=pd.read_csv(file) # all flights
# flights=flights.loc[flights['CANCELLED']==0]
# airlines=set(flights['OP_CARRIER']) # set of names of airlines
#
# # define dataframes
# reasons_vs_airline=pd.DataFrame(index=airlines,columns=['CARRIER_DELAY','WEATHER_DELAY','SECURITY_DELAY','LATE_AIRCRAFT_DELAY'])
# for name in airlines:
#     reasons_vs_airline.loc[name]=0
# for name in airlines:
#     reasons_vs_airline.loc[name]['total_flights'] = flights.loc[flights['OP_CARRIER'] == name].count()['FL_DATE']
#     for reason in list(reasons_vs_airline.columns)[:-1]:
#         reasons_vs_airline.loc[name][reason]=flights.loc[flights['OP_CARRIER']==name].count()[reason]-list(flights.loc[flights['OP_CARRIER']==name][reason]).count(0)
#     reasons_vs_airline.loc[name]=reasons_vs_airline.loc[name].div(reasons_vs_airline.loc[name].sum())
# reasons_vs_airline.sort_values(by='CARRIER_DELAY')
# reasons_vs_airline.to_csv('reasons_vs_airline')
file='reasons_vs_airline'
reasons_vs_airline=pd.read_csv(file,index_col=0,header=0)
airlines=list(reasons_vs_airline.index)
airlines_name={'F9':'Frontier Airlines', '9E':'Endeavor Air', 'EV':'ExpressJet Airlines', 'YX':'Midwest Airlines', 'UA':'United Airlines', 'VX':'Virgin America', 'MQ':'Envoy Air',
               'DL':'Delta Air Lines', 'AA':'American Airlines', 'OO':'SkyWest Airlines', 'YV':'Mesa Airlines', 'HA':'Hawaiian Airlines',
               'AS':'Alaska Airlines', 'OH':'PSA Airlines', 'G4':'Allegiant Air', 'WN':'Southwest Airlines', 'NK':'Spirit Airlines', 'B6':'JetBlue Airways'}
reasons_vs_airline=reasons_vs_airline.rename(index=airlines_name)
airlines=list(reasons_vs_airline.index)
# visualization
bars = np.add(reasons_vs_airline['CARRIER_DELAY'],reasons_vs_airline['WEATHER_DELAY']).tolist()
bars1 = np.add(bars,reasons_vs_airline['SECURITY_DELAY']).tolist()
width=0.4
k=np.arange(len(airlines))
p1 = plt.barh(k,reasons_vs_airline['CARRIER_DELAY'],width)
p2 = plt.barh(k,reasons_vs_airline['WEATHER_DELAY'],width,left=reasons_vs_airline['CARRIER_DELAY'])
p3 = plt.barh(k,reasons_vs_airline['SECURITY_DELAY'],width,left=bars)
p4 = plt.barh(k,reasons_vs_airline['LATE_AIRCRAFT_DELAY'],width,left=bars1)
plt.xticks(np.arange(0, 1.2, 0.1))
plt.yticks(k,airlines)
plt.legend((p1[0], p2[0],p3[0],p4[0]), ('CARRIER_DELAY','WEATHER_DELAY','SECURITY_DELAY','LATE_AIRCRAFT_DELAY'),loc='best')
plt.show()