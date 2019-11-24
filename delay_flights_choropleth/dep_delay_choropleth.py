import pandas as pd
import numpy as np
import plotly.graph_objects as go

# file='2018.csv'
# readlines=10000
# flights=pd.read_csv(file) # all flights
# flights=flights.loc[flights['CANCELLED']==0]
# states=set(flights['ORIGIN_STATE_ABR'])
#
# states_stats=pd.DataFrame(index=states,columns=['dep_delay','arr_delay','total_flights'])
# for state in states:
#     states_stats.loc[state]['dep_delay']=flights.loc[flights['ORIGIN_STATE_ABR']==state]['DEP_DELAY'].mean()
#     states_stats.loc[state]['arr_delay'] = flights.loc[flights['ORIGIN_STATE_ABR'] == state]['ARR_DELAY'].mean()
#     states_stats.loc[state]['total_flights'] = list(flights['ORIGIN_STATE_ABR']).count(state)
# states_stats['state']=states_stats.index
# states_stats.to_csv('states_stats.csv')
file='states_stats.csv'
states_stats=pd.read_csv(file,index_col=0,header=0)
# fig1 = go.Figure(data=go.Choropleth(
#     locations=states_stats['state'], # Spatial coordinates
#     z = states_stats['dep_delay'].astype(float), # Data to be color-coded
#     locationmode = 'USA-states', # set of locations match entries in `locations`
#     colorscale = 'RdBu',
#     marker_line_color='darkgray',
#     marker_line_width=0.5,
#     colorbar_title = "Average departure delay",
# ))
# fig1.update_layout(
#     title_text = '2018 US Average Departure delay by State',
#     geo_scope='usa', # limite map scope to USA
# )
# fig1.show()
fig2 = go.Figure(data=go.Choropleth(
    locations=states_stats['state'], # Spatial coordinates
    z = states_stats['arr_delay'].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale ='Viridis',
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_title = "Average arrival delay",
))
fig2.update_layout(
    title_text = '2018 US Average Arrival delay by State',
    geo_scope='usa', # limite map scope to USA
)
fig2.show()
# fig3 = go.Figure(data=go.Choropleth(
#     locations=states_stats['state'], # Spatial coordinates
#     z = states_stats['total_flights'].astype(float), # Data to be color-coded
#     locationmode = 'USA-states', # set of locations match entries in `locations`
#     colorscale ='Viridis',
#     marker_line_color='darkgray',
#     marker_line_width=0.5,
#     colorbar_title = "Number of flights",
# ))
# fig3.update_layout(
#     title_text = '2018 US Number of flights by State',
#     geo_scope='usa', # limite map scope to USA
# )
# fig3.show()