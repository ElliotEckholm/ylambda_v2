import json
import os
from multiprocessing import Pool
from dotenv import load_dotenv

#load .env variables
load_dotenv('/home/elliot/ylambda/prxmty/.env')

#load custom version of populartimes module
import sys
sys.path.insert(1, '/home/elliot/ylambda/prxmty/elliot_populartimes')
from __init__ import get_id, get

def grab_popularity_data(place):
    google_maps_api_key = os.environ.get('API_KEY')

    popularity_data = get_id(google_maps_api_key, place)
    # print(popularity_data)
    return popularity_data



def prxmty_main(southwest_corner,northeast_corner):
    response = []

    print('southwest_corner')
    print(southwest_corner['latitude'])
    print(southwest_corner['longitude'])
    print('northeast_corner')
    print(northeast_corner['latitude'])
    print(northeast_corner['longitude'])

    # #Testing live data location
    # live_place_id_safeway = 'ChIJzaT-PnlqjoARmdCe0GlYyho'
    # nonlive_place_id_circle_market = 'ChIJD22pcodqjoARovgbcYM2lco'

    # places_list = ['ChIJzaT-PnlqjoARmdCe0GlYyho',
    # 'ChIJD22pcodqjoARovgbcYM2lco','ChIJrTLr-GyuEmsRBfy61i59si0',
    # 'EisxMyBNYXJrZXQgU3RyZWV0LCBXaWxtaW5ndG9uLCBOQyAyODQwMSwgVVNB','ChIJzaT-PnlqjoARmdCe0GlYyho','ChIJD22pcodqjoARovgbcYM2lco',
    # 'ChIJD22pcodqjoARovgbcYM2lco','ChIJrTLr-GyuEmsRBfy61i59si0','ChIJrTLr-GyuEmsRBfy61i59si0',
    # 'ChIJD22pcodqjoARovgbcYM2lco','ChIJrTLr-GyuEmsRBfy61i59si0','ChIJrTLr-GyuEmsRBfy61i59si0',
    # 'ChIJzaT-PnlqjoARmdCe0GlYyho','ChIJD22pcodqjoARovgbcYM2lco','ChIJrTLr-GyuEmsRBfy61i59si0']

    # for place in places_list:
    #     place_response = grab_popularity_data(place)
    #     response.append(place_response)



    google_maps_api_key = os.environ.get('API_KEY')

    # southwest_corner = {"longitude"=-122.02474515885115,"latitude":36.97440808097877}
    # northeast_corner = {"longitude":-122.02454902231692,"latitude":36.974628256252885}

    # response = get(google_maps_api_key, ["grocery_or_supermarket"], (36.97440808097877, -122.02474515885115), (36.974628256252885, -122.02454902231692),n_threads=100,radius=180)


    response = get(google_maps_api_key, ['grocery_or_supermarket','beauty_salon','convenience_store','home_goods_store'], (southwest_corner['latitude'], southwest_corner['longitude']), (northeast_corner['latitude'], northeast_corner['longitude']),n_threads=100,radius=180)

    # response = get_id(google_maps_api_key,"ChIJDU1RcyZAjoARfqpCXYk0QYk")

    return response#data_output[0]['current_popularity']
