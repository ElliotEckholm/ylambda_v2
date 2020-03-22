import populartimes
import json
import os
from multiprocessing import Pool
from dotenv import load_dotenv

#load .env variables
load_dotenv('/home/elliot/ylambda/prxmty/.env')

def grab_popularity_data(place):
    google_maps_api_key = os.environ.get('API_KEY')

    popularity_data = populartimes.get_id(google_maps_api_key, place)
    return popularity_data



def prxmty_main():

    # #Testing live data location
    # live_place_id_safeway = 'ChIJzaT-PnlqjoARmdCe0GlYyho'
    # nonlive_place_id_circle_market = 'ChIJD22pcodqjoARovgbcYM2lco'

    places_list = ['ChIJzaT-PnlqjoARmdCe0GlYyho','ChIJD22pcodqjoARovgbcYM2lco','ChIJrTLr-GyuEmsRBfy61i59si0',
    'EisxMyBNYXJrZXQgU3RyZWV0LCBXaWxtaW5ndG9uLCBOQyAyODQwMSwgVVNB','ChIJzaT-PnlqjoARmdCe0GlYyho','ChIJD22pcodqjoARovgbcYM2lco',
    'ChIJD22pcodqjoARovgbcYM2lco','ChIJrTLr-GyuEmsRBfy61i59si0','ChIJrTLr-GyuEmsRBfy61i59si0',
    'ChIJzaT-PnlqjoARmdCe0GlYyho','ChIJD22pcodqjoARovgbcYM2lco','ChIJrTLr-GyuEmsRBfy61i59si0']

    # for place in places_list:
    #     response = populartimes.get_id(google_maps_api_key, place)
    #     response_array.append(response)

    pool = Pool(len(places_list))                         # Create a multiprocessing Pool
    data_output = pool.map(grab_popularity_data, places_list)



    return data_output
