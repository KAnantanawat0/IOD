import plotly.express as px
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import plotly.io as pio


plot = pd.read_csv('./mental_disorder_per100k_country.csv')

with open('world-countries.json') as f:
    countries_json = json.load(f)



fig = px.choropleth(plot,
                    locations='Country_Name',
                    geojson=countries_json,
                    color='mental_disorder_rate',
                    featureidkey="properties.name",
                    color_continuous_scale='YlOrRd',
                    labels={'mental_disorder_rate':'Mental disorder cases per 100k'})

fig.update_geos(fitbounds="locations", visible=False)
fig.update_coloraxes(colorbar_orientation='h',colorbar_thickness=20)
fig.update_layout(margin={"r":20,"t":0,"l":60,"b":0})


pio.write_image(fig,'fig1.png', width=600, height=400, scale=3)