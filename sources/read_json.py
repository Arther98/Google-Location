import json


def explore_json(data):
    if type(data) is dict:
        for key, value in data.items():
            print(key)
            explore_json(data[key])
    elif type(data) is list:
        for i in range(len(data)):
            explore_json(data[i])
    else:
        print(type(data))

def get_location(location_json, index):
    location = dict()
    location['time'] = location_json.get('locations')[index].get('timestampMs')
    location['lat'] = location_json.get('locations')[index].get('latitudeE7')
    location['lon'] = location_json.get('locations')[index].get('longitudeE7')
    location['acc'] = location_json.get('locations')[index].get('accuracy')
    return location


