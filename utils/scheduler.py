''' This file is used to schedule the tweets '''
import time
import schedule
from tweets.tweet_flights import tweet

def schedule_tweets():
    ''' This function schedules the tweets to be posted every 30 minutes. '''
    schedule.every(30).minutes.do(tweet)
    while True:
        schedule.run_pending()
        time.sleep(1)
