''' This script is used to tweet the flight details of the user. '''
from authenticator import get_twitter_conn_v1, get_twitter_conn_v2
from tweet_formatter import format_tweet
from data.fetch_flight_data import fetch_flight_data

client_v1 = get_twitter_conn_v1()
client_v2 = get_twitter_conn_v2()

#add code for remove previous image and download new image and set to media_path
def tweet():
    ''' This function tweets the flight details of the user. '''
    media_path = r"image.jpg"
    media = client_v1.media_upload(filename=media_path)
    media_id = media.media_id

    detail_data = fetch_flight_data()
    client_v2.create_tweet(text=format_tweet(detail_data), media_ids=[media_id])
