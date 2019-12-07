'''
This file extracts the necessary information from all 2018 flights to create the scoring data
and compiles them into a csv file for each airline according to months.
This allows easier generation of the bar plot. 
'''
import pandas as pd
assert isinstance(file,str)

file='../../data/2018.csv'

flights=pd.read_csv(file) #read file
uncancelled_flights=flights.loc[flights['CANCELLED']==0] #data excluding cancelled flights
airlines=set(flights['OP_CARRIER']) #set of names of airlines

score_data=pd.DataFrame(index=airlines,columns=['op_sch','fl_sp','arr_delay_rate','arr_delay','score'])
for name in airlines:
    score_data.loc[name]['op_sch']=list(flights.loc[flights['OP_CARRIER']==name]['CANCELLED']).count(0)/list(flights['OP_CARRIER']).count(name)
    score_data.loc[name]['fl_sp']=100
    score_data.loc[name]['arr_delay_rate']=1-list(flights.loc[flights['OP_CARRIER']==name]['ARR_DELAY']).count(0)/list(flights['OP_CARRIER']).count(name)
    score_data.loc[name]['arr_delay'] = uncancelled_flights.loc[uncancelled_flights['OP_CARRIER']==name]['ARR_DELAY'].mean()
    score_data.loc[name]['score'] = score_data.loc[name]['op_sch']*score_data.loc[name]['fl_sp']/(1+score_data.loc[name]['arr_delay_rate']*score_data.loc[name]['arr_delay'])
max_score=max(list(score_data['score']))
for name in airlines:
    score_data.loc[name]['score']=score_data.loc[name]['score']/max_score
score_data=score_data.sort_values(by='score')
score_data.to_csv('score_data.csv')
