import json

# Explore the structure of the data.
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)      ### load and store entire set of data in all_eq_data, json.load converts files into something Python can work with

all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []       ### list is made and then loops through dictionary all_eq_dicts
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']      ### each EQ is stored in 'properties' section of this dictionary and under the key 'mag'
    lon = eq_dict['geometry']['coordinates'][0]     ### accesses dictionary representing the geometry element in the EQ
    lat = eq_dict['geometry']['coordinates'][1]     ### second key pulls the list of values associated with coordinates
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])