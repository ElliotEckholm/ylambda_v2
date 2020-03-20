import populartimes
import json

def prxmty_main():

    google_maps_api_key = ''
    #Testing live data location
    live_place_id_safeway = 'ChIJzaT-PnlqjoARmdCe0GlYyho'
    nonlive_place_id_circle_market = 'ChIJD22pcodqjoARovgbcYM2lco'
    response = populartimes.get_id(google_maps_api_key, live_place_id_safeway)

    return response
