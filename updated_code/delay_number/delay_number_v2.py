import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
font = {
#        'family' : 'normal',
#        'weight' : 'bold',
        'size'   :20}
plt.rc('font', **font)


# file='2018.csv'
# flights=pd.read_csv(file) # all flights
# un_flights=flights.loc[flights['CANCELLED']==0]
# airlines=set(flights['OP_CARRIER']) # set of names of airlines
#
# delay_freq=pd.DataFrame(index=airlines,columns=['delay','on-time_and_adv','total_flights'])
# for name in airlines:
#     delay_freq.loc[name]['delay']=un_flights.loc[un_flights['DEP_DELAY']>0].loc[un_flights['OP_CARRIER']==name].count()['FL_DATE']
#     delay_freq.loc[name]['total_flights']=flights.loc[flights['OP_CARRIER']==name].count()['FL_DATE']
#     delay_freq.loc[name]['on-time_and_adv']=delay_freq.loc[name]['total_flights']-delay_freq.loc[name]['delay']
# delay_freq=delay_freq.sort_values(by='on-time_and_adv')
# delay_freq.to_csv('delay_freq')
file='delay_freq'
delay_freq=pd.read_csv(file,index_col=0,header=0)
delay_freq = delay_freq.drop(labels=['AS','EV','F9','G4','HA','NK','VX','YV'])
airlines=list(delay_freq.index)
airlines_name={'F9':'Frontier Airlines', '9E':'Endeavor Air', 'EV':'ExpressJet Airlines', 'YX':'Midwest Airlines', 'UA':'United Airlines', 'VX':'Virgin America', 'MQ':'Envoy Air',
               'DL':'Delta Air Lines', 'AA':'American Airlines', 'OO':'SkyWest Airlines', 'YV':'Mesa Airlines', 'HA':'Hawaiian Airlines',
               'AS':'Alaska Airlines', 'OH':'PSA Airlines', 'G4':'Allegiant Air', 'WN':'Southwest Airlines', 'NK':'Spirit Airlines', 'B6':'JetBlue Airways'}
delay_freq=delay_freq.rename(index=airlines_name)
airlines=list(delay_freq.index)
print(delay_freq)
# visualization
width=0.7
plt.figure(figsize=(10,7))
k=np.arange(len(airlines))
#p1 = plt.barh(delay_freq.index,delay_freq['delay'],width,label='Delay')
#p2 = plt.barh(delay_freq.index,delay_freq['on-time_and_adv'],width,left=delay_freq['delay'],label='On-time/Early')

p1 = plt.barh(k,delay_freq['delay'],width,label='Delay')
p2 = plt.barh(k,delay_freq['on-time_and_adv'],width,left=delay_freq['delay'],label='On-time/Early')
#plt.legend((p1[0], p2[0]), ('Delay number','On-time and advance number'),loc='best')
plt.legend(bbox_to_anchor=(1,-0.4),loc='lower right')
plt.yticks(k,airlines)
ax= plt.axes()
ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:.0f}'.format(x/1000) + 'K'))
plt.xticks(rotation=30)

plt.show()