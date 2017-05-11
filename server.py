import json
import urllib.parse
import urllib.request
import socket

MAPQUEST_API_KEY = 'n1VVYuFNFcNEGPdRBheFtlUjEPLiQmsn'
BASE_URL = 'http://open.mapquestapi.com/directions/v2/'
BASE_URL2 = 'http://open.mapquestapi.com/elevation/v1/'

def build_search_url(src: str, dest: [str]) -> str:

    query_parameters = [
        ('key', MAPQUEST_API_KEY), ('from', src)]

    for i in dest:
        query_parameters.append(('to', i))
    return BASE_URL + '/route?' + urllib.parse.urlencode(query_parameters)

def get_result(url: str) -> dict:

    response = None

    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)

    finally:
        if response != None:
            response.close()

def build_elevation_url(result: dict) -> str:

    query_parameters = [('key', MAPQUEST_API_KEY)]
    to_add = ""
    """
    sub_result = result['route']['locations']
    for i in range(len(sub_result)):
        lat = sub_result[i]['latLng']['lat']
        lng = sub_result[i]['latLng']['lng']
        to_add += str(lat) + "," + str(lng) + ","

    query_parameters.append(('latLngCollection', to_add.rstrip(",")))
    print("HERE", query_parameters)
    """
    query_parameters.append(('sessionId', result['route']['sessionId']))
    print("HERE", query_parameters)
    return BASE_URL2 + '/profile?' + urllib.parse.urlencode(query_parameters)
    

def refine(result: dict, result2: dict) -> dict:

    to_return = {'Steps':[], 'TotalDistance':int, 'TotalTime':int,
                 'LatLong':[], 'Elevation':[]}
    step_guide = result['route']['legs']
    for i in range(len(step_guide)):
        for j in range(len(step_guide[i]['maneuvers'])):
            to_return['Steps'].append(step_guide[i]['maneuvers'][j]['narrative'])
        
    to_return['TotalDistance'] = int(result['route']['distance'])
    to_return['TotalTime'] = int(result['route']['time'])
    
    sub_result = result['route']['locations']
    for i in range(len(sub_result)):
        lat = sub_result[i]['latLng']['lat']
        lng = sub_result[i]['latLng']['lng']
        to_return['LatLong'].append((lat,lng))
        
    for i in range(len(result2['elevationProfile'])):
        to_return['Elevation'].append(result2['elevationProfile'][i]['height'])

    return to_return
