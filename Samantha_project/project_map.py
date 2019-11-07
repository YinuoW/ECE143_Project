#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
"""
Created on Thu Nov  7 00:35:47 2019

@author: Samantha
"""

#Source: https://plot.ly/python/bubble-maps/
from plotly.offline import plot
import plotly.express as px

gapminder = px.data.gapminder().query("year==2007")
fig = px.scatter_geo(gapminder,locations="iso_alpha",color='continent',
                     hover_name = "country", size = "pop",
                     projection = "natural earth")

plot(fig)
'''
# https://plot.ly/python/scatter-plots-on-maps/
import plotly
import plotly.graph_objects as go
import chart_studio.plotly as py
import pandas as pd
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

#Source:https://www.transtats.bts.gov/DL_SelectFields.asp
#Source: https://datahub.io/core/airport-codes#resource-airport-codes_zip
df = pd.read_csv(r'/Users/Samantha/Google Drive/2019_Fall/ECE143/project/airport-codes_zip/data/airport-codes_csv.csv')
#remove duplicates
df.drop_duplicates(subset ="ident", inplace = True) 
#remove airport country name that are not United States 
df.drop(df[df.iso_country != 'US'].index,inplace = True) 

airports_type = ['small_airport','medium_airport','large_airport']
#airports_type = ['large_airport']
df=df[df['type'].isin(airports_type)] 
df.set_index(df.ident,inplace=True)

long_lat= pd.concat([df['coordinates'].str.split(', ', expand=True)], axis=1)
long_lat.set_index(df.ident,inplace=True)

df = pd.DataFrame.join(df,long_lat)
df = df.rename(columns={0: 'long', 1: 'lat'})
df['text'] = df.name+ ', ('+ df.lat + ',' + df.long + ')'

airport2018_lookup = pd.read_csv(r'/Users/Samantha/ECE143_GroupProject/data/airport2018_lookup.csv')
airport2018_lookup.set_index(airport2018_lookup.code)


fig = go.Figure(data=go.Scattergeo(
        locationmode = 'USA-states',
        lon = df['long'],
        lat = df['lat'],
        text = df['text'],
        mode = 'markers'
        #marker_color = df['cnt'],
        ))

fig.update_layout(
        title = 'US airports<br>(Hover for airport names)',
        geo = dict(
            scope='usa',
            projection_type='albers usa',
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5
        ),
    )
plot(fig) #show up in another browser page 
