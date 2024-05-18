''' This file contains the configuration for the application. '''
API_KEY = ''
API_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''
CALLBACK_URL = ''
FLIGHT_LIB_URL = 'https://flight-radar1.p.rapidapi.com/flights/list-in-boundary'
FLIGHT_DETAIL_URL = 'https://flight-radar1.p.rapidapi.com/flights/detail'
FLIGHT_API_HEADERS = {
    "X-RapidAPI-Key": "",
    "X-RapidAPI-Host": "flight-radar1.p.rapidapi.com"
}
FLIGHT_LIB_PARAMS = {
    "bl_lat": "27.569257",
    "bl_lng": "85.154247",
    "tr_lat": "27.839468",
    "tr_lng": "85.555804",
    "limit": "300"
}
