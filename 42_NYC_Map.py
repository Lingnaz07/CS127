#Name Lingna Zheng
#Email LINGNA.ZHENG07@myhunter.cuny.edu
#Date November, 8 2023

import folium 

map = folium.Map(location=[40.75, -74.125], zoom_start=10)

folium.Marker([40.768741,-73.964915],popup="Hunter College").add_to(map)

map.save(outfile ="nycMap.html")
