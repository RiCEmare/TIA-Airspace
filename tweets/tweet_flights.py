import tweepy
from config.config import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
#from data.fetch_flight_data import fetch_flight_data

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def format_tweet():
    flight_no = 'test-flight-123'
    status = 'on time'
    time = '12:00 PM'
    return f"Flight {flight_no} is {status} at {time}."

def tweet_flights():
    #flights = fetch_flight_data()
    #for flight in flights:
    tweet = format_tweet()
    api.update_status(tweet)
