# Import Libraries and Service
from services import Twitter_Service
from playsound import playsound #pip install playsound
from random import shuffle
import time
import sys
import re

import configurations

twitterService = Twitter_Service()

# Initiate Browser
browser = twitterService.initiate_browser()

# Open Twitter Website
twitterService.open_twitter(browser)

# Fill credentials and login
twitterService.login(browser)

read_tweets_response = twitterService.read_file(configurations.tweets_file)
have_tweet = read_tweets_response['have_data']

if have_tweet:

    tweets = read_tweets_response['data']
    print("TWEETS COUNT", len(tweets))

    read_hashtags_response = twitterService.read_file(configurations.hashtags_file)
    have_hashtag = read_hashtags_response['have_data']

    if have_hashtag:
        hashtags = read_hashtags_response['data']
        hashtag_combinations = []
            
        for i in range(len(hashtags)):
            hashtag_combinations.append(twitterService.rotate_hashtags(hashtags, i))

        print("HASHTAG_COMBINATIONS COUNT", len(hashtag_combinations))
        
        hashtagged_tweets = []

        for tweet in tweets:
            for hashtag in hashtag_combinations:
                hashtagged_tweets.append(tweet + hashtag)

        shuffle(hashtagged_tweets)

        print("HASHTAGGED_TWEETS COUNT", len(hashtagged_tweets))

        have_hashtagged_tweets = True

        while (have_hashtagged_tweets):
            have_hashtagged_tweets = not(not hashtagged_tweets)
            
            if have_hashtagged_tweets:
                twitterService.post_tweets(browser, hashtagged_tweets)
                hashtagged_tweets = hashtagged_tweets[1:]
                time.sleep(configurations.tweet_frequency)

            else:
                print("MISSION PASSED! RESPECT +")
                playsound(configurations.music_file)
                time.sleep(1)
        
                twitterService.logout(browser)
                browser.close()
                sys.exit("PROGRAM ENDED!")
                    
    
                