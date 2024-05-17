import schedule
import time
from tweets.tweet_flights import tweet_flights

def schedule_tweets():
    schedule.every(30).minutes.do(tweet_flights)
    while True:
        schedule.run_pending()
        time.sleep(1)
