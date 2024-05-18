import tweepy
from config.config import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from data.fetch_flight_data import fetch_flight_data

client = tweepy.Client(consumer_key=API_KEY, consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)

def format_tweet(detail_data):
    flight_number = detail_data["identification"]["number"]["default"]
    departure_airport = detail_data["airport"]["origin"]["name"]
    arrival_airport = detail_data["airport"]["destination"]["name"]
    scheduled_departure_time = detail_data["time"]["scheduled"]["departure"]
    scheduled_arrival_time = detail_data["time"]["scheduled"]["arrival"]

    return f"Flight {flight_number} from {departure_airport} to {arrival_airport} is scheduled to depart at {scheduled_departure_time} and arrive at {scheduled_arrival_time}."

def tweet_flights():
    detail_data = fetch_flight_data()
    tweet = client.create_tweet(
    text=format_tweet(detail_data)
)
