import json
from datetime import datetime
import read_json


def convert_time_stamp(timestamp):
        print(timestamp)
        print(datetime.fromtimestamp(int(timestamp)/1000))

with open('../json/Locatiegeschiedenis.json') as json_file:
    jsonraw = json.load(json_file)
    location_data = read_json.get_location(jsonraw, 1)
    convert_time_stamp(location_data.get('time'))