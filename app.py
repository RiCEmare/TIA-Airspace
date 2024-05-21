''' This is the main file that will be executed to run the application. '''
from tweets.tweet_flights import tweet

def lambda_handler(event, lambda_context):
    tweet()
