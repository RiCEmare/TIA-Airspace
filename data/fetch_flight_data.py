''' This module fetches flight data from the API and returns the selected flight's detail data. '''
import random
import requests
from config.config import FLIGHT_LIB_URL, FLIGHT_DETAIL_URL, FLIGHT_LIB_PARAMS, FLIGHT_API_HEADERS


def fetch_flight_data():
    ''' select a random flight iwthin the radius and return the selected flight's detail data. '''
    response = requests.get(FLIGHT_LIB_URL, headers=FLIGHT_API_HEADERS,
                            params=FLIGHT_LIB_PARAMS,timeout=20)
    data = response.json()

    if data['aircraft'] != []:
        selected_flight = random.choice(data['aircraft'])
        flight_id = selected_flight[0]
    else:
        return -1
    
    flight_detail_params = {"flight": flight_id}
    detail_response = requests.get(FLIGHT_DETAIL_URL, headers=FLIGHT_API_HEADERS,
        params=flight_detail_params,timeout=20)
    detail_data = detail_response.json()
    return detail_data
