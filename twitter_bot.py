# Import Libraries and Service
from services import Twitter_Service
from playsound import playsound #pip install playsound
import subprocess
import time
import sys

import configurations

twitterService = Twitter_Service()
filename = configurations.init_file

# Initiate Browser
browser = twitterService.initiate_browser()

# Open Twitter Website
twitterService.open_twitter(browser)

# Fill credentials and login
twitterService.login(browser)

action = input("Enter action: Tweet (T) or Like & Retweet (L)? ")

if action.lower() == "t":
    check_data_response = twitterService.read_file(configurations.hashtagged_tweets_file)
    data_exists = check_data_response['have_data']

    if data_exists:
        have_hashtagged_tweets = True

        while (have_hashtagged_tweets):
            read_hashtagged_tweets_response = twitterService.read_file(configurations.hashtagged_tweets_file)
            have_hashtagged_tweets = read_hashtagged_tweets_response['have_data']
            
            if have_hashtagged_tweets:
                hashtagged_tweets = read_hashtagged_tweets_response['data']
                twitterService.post_tweets(browser, hashtagged_tweets)
                
                hashtagged_tweets = hashtagged_tweets[1:]
                
                for i, tweet in enumerate(hashtagged_tweets):
                    tweet = tweet.strip("\n")
                    hashtagged_tweets[i] = tweet
                
                twitterService.write_file(configurations.hashtagged_tweets_file, hashtagged_tweets)
                
                time.sleep(configurations.tweet_frequency)

            else:
                print("MISSION PASSED! RESPECT +")
                playsound(configurations.music_file)
                time.sleep(1)
                
                twitterService.logout(browser)
                browser.close()
                sys.exit("PROGRAM ENDED!")

    else:
        subprocess.Popen('python ' + filename, shell=True).wait()

elif action.lower() == "l":
    query = input("Please enter the hashtag for the tweets you want to search (Case Sensitive): ")
    search_successful = twitterService.search_tweets(browser, query)
    
    if search_successful:
        count = input("How many tweets you want to like/retweet? ")
        twitterService.like_tweets(browser, int(count))

    print("MISSION PASSED! RESPECT +")
    playsound(configurations.music_file)
    time.sleep(1)
                
    twitterService.logout(browser)
    browser.close()
    sys.exit("PROGRAM ENDED!")

                