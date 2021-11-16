import folium
from folium.map import Icon
import pandas

map=folium.Map(location=[47, -118], tiles='Stamen Terrain', zoom_start=6)

fgv=folium.FeatureGroup(name='volcanoes')

df=pandas.read_csv('Volcanoes.txt')
lat=list(df['LAT'])
lon=list(df['LON'])
elev=list(df['ELEV'])
about=list(df['NAME'] + ', ' +df['STATUS']+', '+ df['TYPE'])

def color_picker(elevation):
    if elevation < 2000:
        return 'lightblue'
    elif elevation >= 2000 and elevation < 3000:
        return 'beige'
    else:
        return 'darkred'

for (i,j,k,l) in zip(lat, lon, about, elev):
    fgv.add_child(folium.Marker(location=[i,j], popup=str(l)+' m'+'\n'+ k, 
    icon=folium.Icon(color=color_picker(l))))

fgp=folium.FeatureGroup('population')

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] <10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] <=20000000 else 'red', 'color':'gray'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save('map1.html')
