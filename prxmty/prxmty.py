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

def grab_popularity_from_single_place(place):
    google_maps_api_key = os.environ.get('API_KEY')

    popularity_data = get_id(google_maps_api_key, place)
    # print(popularity_data)
    return popularity_data



def prxmty_main(southwest_corner,northeast_corner):

    google_maps_api_key = os.environ.get('API_KEY')

    place_types = ['airport', 'amusement_park', 'aquarium','art_gallery',
    'bakery','bank','bar','beauty_salon','bicycle_store','book_store',
    'bowling_alley','bus_station','cafe','campground','car_dealer',
    'car_rental','car_repair','car_wash','casino','church','city_hall',
    'clothing_store','convenience_store','courthouse','department_store',
    'doctor','drugstore','electronics_store','florist','furniture_store',
    'gas_station','grocery_or_supermarket','gym','hair_care','hardware_store',
    'home_goods_store','hospital','jewelry_store','laundry','library',
    'liquor_store','lodging','movie_theater','museum','night_club',
    'park','pet_store','pharmacy','post_office','restaurant','rv_park',
    'shopping_mall','spa','stadium','store','supermarket','tourist_attraction',
    'zoo']

    response = get(google_maps_api_key, place_types, (southwest_corner['latitude'], southwest_corner['longitude']),
    (northeast_corner['latitude'], northeast_corner['longitude']),
    n_threads=100,radius=180)

    # response = get_id(google_maps_api_key,"ChIJDU1RcyZAjoARfqpCXYk0QYk")

    return response
