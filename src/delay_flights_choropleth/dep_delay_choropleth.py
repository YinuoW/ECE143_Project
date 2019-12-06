'''
This graph produces the maps of flight delays across the US by state.
'''

import pandas as pd
import plotly.graph_objects as go

## 2018 US Average Departure delay by State
file='states_stats.csv'
states_stats=pd.read_csv(file,index_col=0,header=0)
fig1 = go.Figure(data=go.Choropleth(
    locations=states_stats['state'], # Spatial coordinates
    z = states_stats['dep_delay'].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    #colorscale = 'Rdbu',
    colorscale=[[0.0, "rgb(165,0,38)"],
            [0.1111111111111111, "rgb(215,48,39)"],
            [0.2222222222222222, "rgb(244,109,67)"],
            [0.3333333333333333, "rgb(253,174,97)"],
            [0.4444444444444444, "rgb(254,224,144)"],
            [0.5555555555555556, "rgb(224,243,248)"],
            [0.6666666666666666, "rgb(171,217,233)"],
            [0.7777777777777778, "rgb(116,173,209)"],
            [0.8888888888888888, "rgb(69,117,180)"],
            [1.0, "rgb(49,54,149)"]],
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_title = "Average departure delay",
))
fig1.update_layout(
    title_text = '2018 US Average Departure delay by State',
    geo_scope='usa', # limite map scope to USA
)
fig1.show()

# 2018 US Average Arrival delay by State
fig2 = go.Figure(data=go.Choropleth(
    locations=states_stats['state'], # Spatial coordinates
    z = states_stats['arr_delay'].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale ='Reds',
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_title = "Average arrival delay",
))
fig2.update_layout(
    title_text = '2018 US Average Arrival delay by State',
    geo_scope='usa', # limite map scope to USA
)
fig2.show()

# 2018 US Number of flights by State
fig3 = go.Figure(data=go.Choropleth(
    locations=states_stats['state'], # Spatial coordinates
    z = states_stats['total_flights'].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale ='Reds',
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_title = "Number of flights",
))
fig3.update_layout(
    title_text = '2018 US Number of flights by State',
    geo_scope='usa', # limite map scope to USA
)
fig3.show()
