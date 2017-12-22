import folium
import pandas as pd

data=pd.read_csv('Volcanoes_USA.txt', sep=',')
lat=list(data['LAT'])
lon=list(data['LON'])
elev=list(data['ELEV'])

def color_producer(elevation):
    if elevation < 1000:
        return ['green','lime']
    elif 1000 <= elevation < 3000:
        return ['orangered','orange']
    else:
        return ['crimson','red']

map = folium.Map(location=[38.88,-99.09],zoom_start=6,tiles='Mapbox Bright')

fgv = folium.FeatureGroup(name='Volcanoes')

for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],popup=folium.Popup(str(el)+' m',parse_html=True),\
    color=color_producer(el)[0],radius=6,fill=True,fill_color=color_producer(el)[1],\
    fill_opacity=0.7))

fgp = folium.FeatureGroup(name='Population')

fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),\
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000\
else 'orange' if 1000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save('map1.html')
