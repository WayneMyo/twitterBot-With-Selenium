# Import Libraries and Service
from services import Twitter_Service
import subprocess
import configurations

twitterService = Twitter_Service()
filename = configurations.bot_file

read_tweets_response = twitterService.read_file(configurations.tweets_file)
have_tweet = read_tweets_response['have_data']

if have_tweet:
    tweets = read_tweets_response['data']
    print("TWEETS COUNT", len(tweets))

    read_hashtags_response = twitterService.read_file(configurations.hashtags_file)
    have_hashtag = read_hashtags_response['have_data']

    if have_hashtag:
        hashtags = read_hashtags_response['data']
        print("HASHTAGS COUNT", len(hashtags))

        hashtag_combinations = []
            
        for i in range(len(hashtags)):
            hashtag_combinations.append(twitterService.rotate_hashtags(hashtags, i))

        print("HASHTAG_COMBINATIONS COUNT", len(hashtag_combinations))

        hashtagged_tweets = []

        for tweet in tweets:
            tweet = tweet.strip("\n") + " "
            for hashtag in hashtag_combinations:
                hashtagged_tweets.append(tweet + hashtag)

        print("HASHTAGGED TWEETS COUNT", len(hashtagged_tweets))

        twitterService.write_file(configurations.hashtagged_tweets_file, hashtagged_tweets)
        subprocess.Popen('python ' + filename, shell=True).wait()

    else:
        print("NO HASHTAG FOUND!")

else:
    print("NO TWEET FOUND!")