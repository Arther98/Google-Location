#modules
import json
import gmplot

#submodules
from datetime import datetime

#own py files
import read_json


def convert_time_stamp(timestamp):
        return(datetime.fromtimestamp(int(timestamp)/1000))

def plot(lat_list, lon_list):
     gmap = gmplot.GoogleMapPlotter(51.754030, 5.130150, 13)
     gmap.scatter(lon_list, lat_list, '# FF0000', size = 40, marker = False)
     gmap.plot(lon_list, lat_list, 'cornflowerblue', edge_width = 2.5)
     gmap.draw("C:\\Users\\ArthervdBerg\\git\\Google-Location\\output\\map.html")

with open('../json/Locatiegeschiedenis.json') as json_file:
    json_raw = json.load(json_file)
    lat_list = list()
    lon_list = list()

    for i in range(len(json_raw.get('locations'))):
        if(i < 5):
            location_data = read_json.get_location(json_raw, i)
            lat_list.append(location_data.get('lat'))
            lon_list.append(location_data.get('lon'))


    gmpap = plot(lat_list, lon_list)

