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

keylist = ['Southwest Airlines Co.', 'JetBlue Airways', 'Endeavor Air Inc.', 'PSA Airlines Inc.', 'United Air Lines Inc.', 'Mesa Airlines Inc.', 'ExpressJet Airlines Inc.', 'Envoy Air', 'Spirit Air Lines', 'Alaska Airlines Inc.', 'Republic Airline', 'American Airlines Inc.', 'Allegiant Air', 'SkyWest Airlines Inc.', 'Delta Air Lines Inc.', 'Frontier Airlines Inc.', 'Hawaiian Airlines Inc.', 'Virgin America']

carrier_delay = list()
for i in keylist[0:10]:
    for key in code_name:
        if code_name[key] == i:
            i = key
    carrier_delay.append(df.loc[df['OP_CARRIER']==i]['CARRIER_DELAY'].sum())

whether_delay = list()
for i in keylist[0:10]:
    for key in code_name:
        if code_name[key] == i:
            i = key
    whether_delay.append(df.loc[df['OP_CARRIER']==i]['WEATHER_DELAY'].sum())

aircraft_delay = list()
for i in keylist[0:10]:
    for key in code_name:
        if code_name[key] == i:
            i = key
    aircraft_delay.append(df.loc[df['OP_CARRIER']==i]['LATE_AIRCRAFT_DELAY'].sum())

nas_delay = list()
for i in keylist[0:10]:
    for key in code_name:
        if code_name[key] == i:
            i = key
    nas_delay.append(df.loc[df['OP_CARRIER']==i]['NAS_DELAY'].sum())

security_delay = list()
for i in keylist[0:10]:
    for key in code_name:
        if code_name[key] == i:
            i = key
    security_delay.append(df.loc[df['OP_CARRIER']==i]['SECURITY_DELAY'].sum())

fig = go.Figure(go.Bar(x=keylist[0:10], y=carrier_delay, name='Carrier delay',marker_color='goldenrod'))
fig.add_trace(go.Bar(x=keylist[0:10], y=security_delay, name='Security delay'))
fig.add_trace(go.Bar(x=keylist[0:10], y=whether_delay, name='Weather delay',marker_color='burlywood'))
fig.add_trace(go.Bar(x=keylist[0:10], y=aircraft_delay, name='Aircraft delay',marker_color='saddlebrown'))
fig.add_trace(go.Bar(x=keylist[0:10], y=nas_delay, name='NAS delay',marker_color='darkorange'))

fig.update_layout(title='Delay reasons for each airline',
                    yaxis={'title':'Time'},
                  barmode='stack', xaxis={'categoryorder':'array', 'categoryarray':keylist[0:10]})
fig.show()