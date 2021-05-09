import tweepy
import ssl
import pandas as pd
import pprint
import json
import sys
import os



consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""


search_terms = ['#debateTelemadrid']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def stream_tweets(search_term):
    data = [] # empty list to which tweet_details obj will be added
    counter = 0 # counter to keep track of each iteration
    for tweet in tweepy.Cursor(api.search, q='\"{}\" -filter:retweets'.format(search_term), count=5000, lang='es', tweet_mode='extended', encoding='utf-8').items():
        tweet_details = {}
        tweet_details['name'] = tweet.user.screen_name
        tweet_details['tweet'] = tweet.full_text
        tweet_details['retweets'] = tweet.retweet_count
        tweet_details['created'] = tweet.created_at.strftime("%m/%d/%Y, %H:%M:%S")
        tweet_details['followers'] = tweet.user.followers_count
        tweet_details['is_user_verified'] = tweet.user.verified     
        tweet_details['favorite_count'] = tweet.favorite_count
        tweet_details['favorited'] = tweet.favorited
        tweet_details['retweeted'] = tweet.retweeted

        data.append(tweet_details)
        print(tweet.created_at, '-', tweet.full_text)
        counter += 1
        if counter == 10:
            break
        else:
            print("couter :", counter)
            pass
    try:
        os.makedirs('data')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    with open('data/{}.json'.format(search_term), 'w') as f:
        json.dump(data, f)
    print('done!')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        search_terms = [f"#{sys.argv[1]}"]
    print(search_terms)
    print('Starting to stream...')
    for search_term in search_terms:
        stream_tweets(search_term)
    print('finished!')