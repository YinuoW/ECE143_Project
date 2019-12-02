# This file generates the delay and ontime number of flights for each airline

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file='delay_freq.csv'
delay_freq=pd.read_csv(file,index_col=0,header=0)
airlines=list(delay_freq.index)
airlines_name={'F9':'Frontier Airlines', '9E':'Endeavor Air', 'EV':'ExpressJet Airlines', 'YX':'Midwest Airlines', 'UA':'United Airlines', 'VX':'Virgin America', 'MQ':'Envoy Air',
               'DL':'Delta Air Lines', 'AA':'American Airlines', 'OO':'SkyWest Airlines', 'YV':'Mesa Airlines', 'HA':'Hawaiian Airlines',
               'AS':'Alaska Airlines', 'OH':'PSA Airlines', 'G4':'Allegiant Air', 'WN':'Southwest Airlines', 'NK':'Spirit Airlines', 'B6':'JetBlue Airways'}
delay_freq=delay_freq.rename(index=airlines_name)
airlines=list(delay_freq.index)
print(delay_freq)
# visualization
width=0.4
k=np.arange(len(airlines))
p1 = plt.barh(k,delay_freq['delay'],width)
p2 = plt.barh(k,delay_freq['on-time_and_adv'],width,left=delay_freq['delay'])
plt.legend((p1[0], p2[0]), ('Delay number','On-time and advance number'),loc='best')
plt.yticks(k,airlines)
plt.show()