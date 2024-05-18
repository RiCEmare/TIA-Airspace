''' This module is used to authenticate the user to the Twitter API. '''
import tweepy
from config.config import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

def get_twitter_conn_v1() -> tweepy.API:
    ''' Get twitter conn 1.1 '''

    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET)
    auth.set_access_token(
        ACCESS_TOKEN,
        ACCESS_TOKEN_SECRET,
    )
    return tweepy.API(auth)

def get_twitter_conn_v2() -> tweepy.Client:
    ''' Get twitter conn 2.0 '''

    client = tweepy.Client(
        consumer_key=API_KEY,
        consumer_secret=API_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET,
    )

    return client
