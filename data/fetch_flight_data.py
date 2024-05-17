import requests
from config.config import FLIGHT_API_URL

def fetch_flight_data():
    response = requests.get(FLIGHT_API_URL, timeout=10)  # Add timeout argument
    return response.json()
