import folium
# from folium import plugins
# from folium.features import CustomIcon
import top_stations

# stop_id,stop_code,stop_name,stop_desc,stop_lat,stop_lon

coordinates = []
station_name = []
with open("DMRC_GTFS/stops.txt") as f:
    for i in range(262):
        coordinates.append(tuple(map(float, f.readline().split(',,')[2].split(','))))

with open("DMRC_GTFS/stops.txt") as f:
    for i in range(262):
        station_name.append(f.readline().split(',,')[1])

top_station_showing = []
for i in top_stations.keys:
    try:
        top_station_showing.append(station_name.index(i))
    except:
        pass

m = folium.Map(location=coordinates[0], zoom_start= 5)

for i in coordinates:
    if i not in top_stations.keys:
        folium.Marker(i, popup=f"Latitude : {i[0]}, Longitude : {i[1]}").add_to(m)

for i in top_station_showing:
    folium.Marker(coordinates[i], popup=f"Latitude : {coordinates[i][0]}, Longitude : {coordinates[i][1]}", icon=folium.Icon(color="red")).add_to(m)
# for i in top_stations.keys

m.save("maps.html")
m