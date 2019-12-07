'''
This file creates the bar chart distribution for each delay reason for all airlines.
'''

import pandas as pd
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

keylist=['Southwest Airlines Co.', 'Delta Air Lines Inc.', 'American Airlines Inc.', 'SkyWest Airlines Inc.', 'United Air Lines Inc.', 'Republic Airline', 'JetBlue Airways', 'Envoy Air', 'PSA Airlines Inc.', 'Endeavor Air Inc.', 'Alaska Airlines Inc.', 'Mesa Airlines Inc.', 'ExpressJet Airlines Inc.', 'Spirit Air Lines', 'Frontier Airlines Inc.', 'Allegiant Air', 'Hawaiian Airlines Inc.', 'Virgin America']

carrier_delay = list()
for i in keylist[0:10]:
    for key in code_name:
        if code_name[key] == i:
            i = key
    carrier_delay.append(df.loc[df['OP_CARRIER']==i]['CARRIER_DELAY'].sum())
print(carrier_delay)

whether_delay = list()
for i in keylist[0:10]:
    for key in code_name:
        if code_name[key] == i:
            i = key
    whether_delay.append(df.loc[df['OP_CARRIER']==i]['WEATHER_DELAY'].sum())
print(whether_delay)

aircraft_delay = list()
for i in keylist[0:10]:
    for key in code_name:
        if code_name[key] == i:
            i = key
    aircraft_delay.append(df.loc[df['OP_CARRIER']==i]['LATE_AIRCRAFT_DELAY'].sum())
print(aircraft_delay)

nas_delay = list()
for i in keylist[0:10]:
    for key in code_name:
        if code_name[key] == i:
            i = key
    nas_delay.append(df.loc[df['OP_CARRIER']==i]['NAS_DELAY'].sum())
print(nas_delay)


security_delay = list()
for i in keylist[0:10]:
    for key in code_name:
        if code_name[key] == i:
            i = key
    security_delay.append(df.loc[df['OP_CARRIER']==i]['SECURITY_DELAY'].sum())
print(security_delay)

fig = go.Figure(go.Bar(x=keylist[0:10], y=carrier_delay, name='Carrier delay',marker_color='goldenrod'))
fig.add_trace(go.Bar(x=keylist[0:10], y=security_delay, name='Security delay'))
fig.add_trace(go.Bar(x=keylist[0:10], y=whether_delay, name='Weather delay',marker_color='burlywood'))
fig.add_trace(go.Bar(x=keylist[0:10], y=aircraft_delay, name='Aircraft delay',marker_color='saddlebrown'))
fig.add_trace(go.Bar(x=keylist[0:10], y=nas_delay, name='NAS delay',marker_color='darkorange'))

fig.update_layout(title='Delay reasons for each airline',
                    yaxis={'title':'Time'},
                  barmode='stack', xaxis={'categoryorder':'array', 'categoryarray':keylist[0:10]})
fig.show()
