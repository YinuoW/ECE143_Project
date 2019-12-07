'''
This file generates the bar chart of the total flights for each airline.
Input file: 2018.csv, airline2018_lookup.csv

'''
import pandas as pd
from plotly.offline import iplot, init_notebook_mode
import plotly.graph_objs as go

data_dir = "../../data/2018.csv"
airline2018_dir = '../../data/airline2018_lookup.csv'
df_airline2018 = pd.read_csv(airline2018_dir)
df = pd.read_csv(data_dir)

airlines_code = list(df_airline2018['Code'])
airlines_name = list(df_airline2018['Description'])

code_name = dict()
for idx, air in enumerate(airlines_code):
    code_name[air] = airlines_name[idx]

df4 = df.loc[:,['OP_CARRIER']]
df4['OP_CARRIER'] = df4['OP_CARRIER'].replace(code_name)

airline_group = df4.groupby(['OP_CARRIER'])['OP_CARRIER'].count().sort_values(ascending=False)
trace = go.Bar(x=airline_group[:10].index,
                y=airline_group[:10].values,
                name='airlines',
                marker={
                    'color':airline_group[:10].values,
                    'colorscale':'Oranges',
                    'showscale':True,
                    },
                )

layout = go.Layout(title='Number of Flights of Airlines',
                    xaxis={'title':'Airlines'},
                    yaxis={'title':'Number of Flights'},
                    autosize=False,
                    width=800,
                    height=500,
                    margin=go.layout.Margin(
                        l=50,
                        r=40,
                        b=80,
                        t=80,
                        pad=4
                    ))

fig = go.Figure(data=[trace], layout=layout)
iplot(fig, filename='airline_bar')
