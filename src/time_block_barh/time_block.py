'''
This plot generates the delays for each time block as follows:
1. 6am to 12pm
2. 12pm to 6 pm
3. 6pm to 6am
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file='time_block.csv'
time_block=pd.read_csv(file,index_col=0,header=0)

time_block = time_block.drop(labels=['AS','EV','F9','G4','HA','NK','VX','YV'])
airlines=list(time_block.index)
airlines_name={'F9':'Frontier Airlines', '9E':'Endeavor Air', 'EV':'ExpressJet Airlines',
               'YX':'Midwest Airlines', 'UA':'United Airlines', 'VX':'Virgin America', 'MQ':'Envoy Air',
               'DL':'Delta Air Lines', 'AA':'American Airlines', 'OO':'SkyWest Airlines',
               'YV':'Mesa Airlines', 'HA':'Hawaiian Airlines',
               'AS':'Alaska Airlines', 'OH':'PSA Airlines', 'G4':'Allegiant Air',
               'WN':'Southwest Airlines', 'NK':'Spirit Airlines', 'B6':'JetBlue Airways'}

time_block['sum'] = time_block.sum(axis=1)

time_block=time_block.rename(index=airlines_name)

time_block=time_block.sort_values(by=['sum'],ascending=False)

airlines=list(time_block.index)
print(time_block)
width=0.2

d1=np.array(time_block['morning'])
d2=np.array(time_block['afternoon'])
d3=np.array(time_block['night'])
plt.figure(figsize=(10,7))

x=np.arange(len(airlines))
p1=plt.barh(x,d1,color ='#D3716E',lw=2)
p2=plt.barh(x,d2,color='#70A9A1',left=d1,lw=2)
p3=plt.barh(x,d3,left=d2+d1,lw=2,color='#A5D1AB')
plt.yticks(x,airlines)

plt.legend((p1[0], p2[0],p3[0]), ('6am to 12pm','12pm to 6 pm','6pm to 6am'),loc='best')


plt.xlabel('Average delays')
plt.title('Average delay time block')
font = {'size':20}

plt.rc('font', **font)
plt.show()
