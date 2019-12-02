import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file='2018.csv'
readlines=100000
flights=pd.read_csv(file) # all flights
flights=flights.loc[flights['CANCELLED']==0]
flights=flights.sort_values(by='DEP_TIME_BLK')
cm = plt.cm.get_cmap('winter')
plt1=plt.scatter(x=flights['DEP_DELAY'],y=flights['DEP_TIME_BLK'],c=flights['DEP_DELAY'],cmap=cm)
plt.colorbar(plt1)
plt.ylabel('Departure time block')
plt.xlabel('Departure delay')
plt.title('Departure delay vs Departure time block')
plt.show()