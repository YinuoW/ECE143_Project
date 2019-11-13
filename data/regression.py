#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 21:14:28 2019

@author: Samantha
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



file='./2018.csv'
data=pd.read_csv(file) #read file

uncancelled_flights=data.loc[data['CANCELLED']==0] #data excluding cancelled flights
airlines=set(data['OP_CARRIER']) #set of names of airlines

data['FL_DATE'] = pd.to_datetime(data['FL_DATE']).dt.date

data_top = data.head()  
list(data.columns)
'''
df_train = df[df['SCHEDULED_DEPARTURE'].apply(lambda x:x.date()) < datetime.date(2015, 1, 23)]
df_test  = df[df['SCHEDULED_DEPARTURE'].apply(lambda x:x.date()) > datetime.date(2015, 1, 23)]
df = df_train


carrier = 'AA'
check_airports = df[(df['OP_CARRIER'] == carrier)]['DEPARTURE_DELAY'].groupby(df['ORIGIN']).apply(get_stats).unstack()
check_airports.sort_values('count', ascending = False, inplace = True)
check_airports[-5:]
'''