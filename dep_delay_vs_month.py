import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file='2018_date_index.csv'
flights=pd.read_csv(file,nrows=10000)
airlines=set(flights['OP_CARRIER']) # set of names of airlines
flights=flights.set_index('FL_DATE')
# airline delay vs date
airlines_delay_vs_month=pd.DataFrame(index=airlines,columns=list(range(1,13)))
for name in airlines:
    for i in range(1,2):
        if i == 1 or 3 or 5 or 7 or 8:
            airlines_delay_vs_month.loc[name, i] =flights.loc['2018-0' + str(i) + '-01':'2018-0' + str(i) + '-31'].loc[flights['OP_CARRIER'] == name]['DEP_DELAY'].mean()
        if i == 10 or 12:
            airlines_delay_vs_month.loc[name, i] =flights.loc['2018-' + str(i) + '-01':'2018-' + str(i) + '-31'].loc[flights['OP_CARRIER'] == name]['DEP_DELAY'].mean()
        if i == 4 or 6 or 9:
            airlines_delay_vs_month.loc[name, i] =flights.loc['2018-0' + str(i) + '-01':'2018-0' + str(i) + '-30'].loc[flights['OP_CARRIER'] == name]['DEP_DELAY'].mean()
        if i == 11:
            airlines_delay_vs_month.loc[name, i] =flights.loc['2018-' + str(i) + '-01':'2018-' + str(i) + '-30'].loc[flights['OP_CARRIER'] == name]['DEP_DELAY'].mean()
        if i == 2:
            airlines_delay_vs_month.loc[name, i] =flights.loc['2018-02-01':'2018-02-28'].loc[flights['OP_CARRIER'] == name]['DEP_DELAY'].mean()
print(airlines_delay_vs_month)

# visualization
airlines_delay_vs_month.loc['AA'].plot(kind='line')

#show plots
plt.show()