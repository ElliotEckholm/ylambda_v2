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



def prxmty_main(rectangle):
    response = []

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


    # pool = Pool(20)                         # Create a multiprocessing Pool
    # response = pool.map(grab_popularity_data, places_list)
    # pool.close()
    # pool.join()

    google_maps_api_key = os.environ.get('API_KEY')
    response = get(google_maps_api_key, ["bar"], (48.132986, 11.566126), (48.134199, 11.580047),n_threads=100,radius=180)



    return response#data_output[0]['current_popularity']
