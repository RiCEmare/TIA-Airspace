''' This script is used to tweet the flight details of the user. '''
import random
from tweets.authenticator import get_twitter_conn_v1, get_twitter_conn_v2
from tweets.image_downloader import download_image
from tweets.tweet_formatter import format_tweet, safe_get
from data.fetch_flight_data import fetch_flight_data

client_v1 = get_twitter_conn_v1()
client_v2 = get_twitter_conn_v2()

#add code for remove previous image and download new image and set to media_path
def tweet():
    ''' This function tweets the flight details of the user. '''
    if fetch_flight_data() != -1:
        detail_data = fetch_flight_data()
        tweet_text = format_tweet(detail_data)
    else:
        tweet_text = "Currently there are no flights in the airspace. Here's a picture of a cat instead. 😻"
        url = 'https://cataas.com/cat'
        media_path = download_image(url,aircraft=False)
        media = client_v1.media_upload(filename=media_path)
        media_id = media.media_id
        return client_v2.create_tweet(text=tweet_text, media_ids=[media_id])

    thumbnail = safe_get(detail_data, ['aircraft', 'images', 'thumbnails'])
    if thumbnail != 'null':
        selected_image = random.choice(detail_data['aircraft']['images']['thumbnails'])
        url = selected_image['src']
        media_path = download_image(url)
        media = client_v1.media_upload(filename=media_path)
        media_id = media.media_id
        return client_v2.create_tweet(text=tweet_text, media_ids=[media_id])
    else:
        return client_v2.create_tweet(text=tweet_text)
