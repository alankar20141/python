import tweepy
from tweepy import OAuthHandler
import json

consumer_key = '0P93fhFbZ8Q0x9kvuysZsZMl1'
consumer_secret = '8TVdGm1sOPzchNkqvgpHrpB0vGY9lBDllYAzWF8VlxZaOIpuHy'
access_token = '3266814258-DNm55gABwJcRcCm35YWVCiqNarlZ4B9d6zul4DO'
access_secret = 'rQElYcX0msYWR5eJLXUGgaggWNZH9UaG5VryH5wK6Hjme'

auth =OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api=tweepy.API(auth)

def process_or_store(tweet):
    print(json.dumps(tweet))

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    process_or_store(status._json)
    
    
    

