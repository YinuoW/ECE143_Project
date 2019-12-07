'''
This file generates the graphs for the score of each airline based the csv file.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
assert isinstance(file,str)

file='score_data.csv'
score_data=pd.read_csv(file,index_col=0,header=0)
airlines=list(score_data.index)
airlines_name={'F9':'Frontier Airlines', '9E':'Endeavor Air', 'EV':'ExpressJet Airlines', 'YX':'Midwest Airlines', 'UA':'United Airlines', 'VX':'Virgin America', 'MQ':'Envoy Air',
               'DL':'Delta Air Lines', 'AA':'American Airlines', 'OO':'SkyWest Airlines', 'YV':'Mesa Airlines', 'HA':'Hawaiian Airlines',
               'AS':'Alaska Airlines', 'OH':'PSA Airlines', 'G4':'Allegiant Air', 'WN':'Southwest Airlines', 'NK':'Spirit Airlines', 'B6':'JetBlue Airways'}
score_data=score_data.rename(index=airlines_name)
x=np.arange(len(airlines))
plt.barh(x,score_data['score'],ec='grey',fc='lightblue',tick_label=score_data.index)
for (i,j) in zip(score_data['score'],x):
    plt.text(i+0.02, j-0.2, '%.2f' % i )
plt.xlim(0,1.1)
plt.xticks(np.arange(0,1.1,step=0.2))
plt.xlabel('Scores')
plt.ylabel('Airlines')
plt.title('Score of airlines')
plt.show()
