import random
import requests
from config.config import FLIGHT_LIB_URL, FLIGHT_DETAIL_URL, FLIGHT_LIB_PARAMS, FLIGHT_API_HEADERS


def fetch_flight_data():
    response = requests.get(FLIGHT_LIB_URL, headers=FLIGHT_API_HEADERS,
                            params=FLIGHT_LIB_PARAMS,timeout=20)
    data = response.json()
    selected_flight = random.choice(data['aircraft'])
    flight_id = selected_flight[0]

    FLIGHT_DETAIL_PARAMS = {"flight": flight_id}
    detail_response = requests.get(FLIGHT_DETAIL_URL, headers=FLIGHT_API_HEADERS,
        params=FLIGHT_DETAIL_PARAMS,timeout=20)
    detail_data = detail_response.json()
    return detail_data
