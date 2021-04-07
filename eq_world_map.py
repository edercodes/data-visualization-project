import json

from plotly.graph_objs import Scattergeo, Layout       ### imports Scattergeo chart 'type' and Layout 'class'
from plotly import offline

# Explore the structure of the data.
filename = 'data/eq_data_30_day_m1.json'        ### file adjusted for 30 day time frame
with open(filename) as f:
    all_eq_data = json.load(f)      ### load and store entire set of data in all_eq_data, json.load converts files into something Python can work with

all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts = [], [], [], []       ### list is made and then loops through dictionary all_eq_dicts
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']      ### each EQ is stored in 'properties' section of this dictionary and under the key 'mag'
    lon = eq_dict['geometry']['coordinates'][0]     ### accesses dictionary representing the geometry element in the EQ
    lat = eq_dict['geometry']['coordinates'][1]     ### second key pulls the list of values associated with coordinates
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {     ### specifies how big each marker should be, one of many customizations Plotly offers
        'size': [5*mag for mag in mags],        ### multiplies the magnitude of EQ mag by a scale factor to get appopriate marker size for the map
        'color': mags,
        'colorscale': 'Viridis',        ### tells Plotly to use range of colors Viridis, range from blue to yellow
        'reversescale': True,        ### 'reversescale' to set lowest values for yelloe and blue for severe EQs
        'colorbar': {'title': 'Magnitude'},
    },
}]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}       ### gives appropriate title and creates a dictionary called fig to contain data and layoutß
offline.plot(fig, filename='global_earthquakes.html')

print(mags[:10])
print(lons[:5])
print(lats[:5])