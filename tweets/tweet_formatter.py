''' This module contains functions to format the tweet data. '''
from datetime import datetime

def timestamp_to_datetime(timestamp):
    ''' This function converts the timestamp to a human-readable datetime format.'''
    dt_object = datetime.fromtimestamp(timestamp)
    return dt_object.strftime("%Y/%m/%d %I:%M %p")

def format_tweet(detail_data):
    ''' This function creates the tweet from the detail data.'''

    airline = detail_data["airline"]["short"]
    flight_number = detail_data["identification"]["number"]["default"]
    departure_airport = detail_data["airport"]["origin"]["name"]
    arrival_airport = detail_data["airport"]["destination"]["name"]
    scheduled_departure_time = timestamp_to_datetime(detail_data["time"]["scheduled"]["departure"])
    scheduled_arrival_time = timestamp_to_datetime(detail_data["time"]["scheduled"]["arrival"])
    status = detail_data["status"]["generic"]["status"]["text"]
    if status == "arrived":
        return f"{airline} Flight {flight_number} from {departure_airport} to {arrival_airport} arrived at {scheduled_arrival_time}."
    elif status == "scheduled":
        return f"{airline} Flight {flight_number} from {departure_airport} to {arrival_airport} is scheduled to depart at {scheduled_departure_time} and arrive at {scheduled_arrival_time}."
    elif status == "cancelled":
        return f"{airline} Flight {flight_number} from {departure_airport} to {arrival_airport} has been cancelled."
    elif status == "diverted":
        return f"{airline} Flight {flight_number} from {departure_airport} to {arrival_airport} has been diverted."
    elif status == "delayed":
        return f"{airline} Flight {flight_number} from {departure_airport} to {arrival_airport} has been delayed."
    else:
        return f"{airline} Flight {flight_number} from {departure_airport} to {arrival_airport} is {status}."
