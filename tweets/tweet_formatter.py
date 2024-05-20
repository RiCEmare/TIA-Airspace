''' This module contains functions to format the tweet data. '''
from datetime import datetime, timezone, timedelta
import google.generativeai as genai
from config.config import GEMINI_API_KEY

def safe_get(data, keys, default='null'):
    ''' This function safely gets the value from the json.'''
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key, default)
        else:
            return default
    return data if data is not None else default

def format_timestamp(timestamp):
    ''' This function converts the timestamp to a UTC+5:45 datetime format.'''
    if timestamp == 'null':
        return 'null'
    utc_time = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    nepal_time = utc_time.astimezone(timezone(timedelta(hours=5, minutes=45)))
    return nepal_time.strftime("%I:%M %p")

def format_tweet(detail_data):
    ''' This function creates the tweet from the detail data.'''

    flight_number = safe_get(detail_data, ['identification', 'number', 'default'])
    airline_name = safe_get(detail_data, ['airline', 'name'])
    origin_name = safe_get(detail_data, ['airport', 'origin', 'name'])
    destination_name = safe_get(detail_data, ['airport', 'destination', 'name'])
    scheduled_departure = safe_get(detail_data, ['time', 'scheduled', 'departure'])
    scheduled_arrival = safe_get(detail_data, ['time', 'scheduled', 'arrival'])
    status_text = safe_get(detail_data, ['status', 'text'])
    real_departure = safe_get(detail_data, ['time', 'real', 'departure'])
    real_arrival = safe_get(detail_data, ['time', 'real', 'arrival'])
    estimated_arrival = safe_get(detail_data, ['time', 'estimated', 'arrival'])
    scheduled_departure_time = format_timestamp(scheduled_departure)
    scheduled_arrival_time = format_timestamp(scheduled_arrival)
    real_departure_time = format_timestamp(real_departure)
    real_arrival_time = format_timestamp(real_arrival)
    estimated_arrival_time = format_timestamp(estimated_arrival)

    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"""
    Create a tweet for a bot which posts info of a random flight.
    Flight Number: {flight_number}
    Airline: {airline_name}
    Origin: {origin_name}
    Destination: {destination_name}
    Status: {status_text}
    Scheduled Departure Time: {scheduled_departure_time}
    Scheduled Arrival Time: {scheduled_arrival_time}
    Real Departure Time: {real_departure_time}
    Real Arrival Time: {real_arrival_time}
    Estimated Arrival Time: {estimated_arrival_time}
    The tweet should be informative, fun, and under 280 characters. Create sentences. No hashtags or links. Include flag emojis of the origin and destination countries. No further updates. 
    """
    response = model.generate_content(prompt)
    return response.text
