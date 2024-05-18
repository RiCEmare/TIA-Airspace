''' This script is used to tweet the flight details of the user. '''
import random
from tweets.authenticator import get_twitter_conn_v1, get_twitter_conn_v2
from tweets.image_downloader import download_image
from tweets.tweet_formatter import format_tweet
from data.fetch_flight_data import fetch_flight_data

client_v1 = get_twitter_conn_v1()
client_v2 = get_twitter_conn_v2()

#add code for remove previous image and download new image and set to media_path
def tweet():
    ''' This function tweets the flight details of the user. '''
    detail_data = fetch_flight_data()

    selected_image = random.choice(detail_data['aircraft']['images']['thumbnails'])
    url = selected_image['src']
    media_path = download_image(url)
    media = client_v1.media_upload(filename=media_path)
    media_id = media.media_id

    client_v2.create_tweet(text=format_tweet(detail_data), media_ids=[media_id])
