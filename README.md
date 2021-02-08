# twitterBot With Selenium
Twitter Bot that you can schedule your tweets

<b>Dependencies</b>
- [Python3](https://www.python.org/downloads/)
- [selenium](https://pypi.org/project/selenium/)
- [webdriver-manager](https://pypi.org/project/webdriver-manager/)
- [playsound](https://pypi.org/project/playsound/)

## To run the code
- Install all dependencies
- Open configurations.py
- Fill up your twitter credentials inside configurations.py and save
- Prepare tweets in tweets.txt
- Prepare hashtags in hashtags.txt
- Open Command Prompt
- Type in the Command Prompt: cd the directory where twitter_ bot.py is. (Eg: cd C:\Users\user\Download\twitterBot-With-Selenium)
- Type python twitter_bot.py in Command Prompt

## To change tweet frequency
- Change the value of tweet_frequency variable inside configurations.py (line 10 of configurations.py)

### If you do not want to shuffle hashtags and multiply tweets
Please put hashtags in one line inside hashtags.txt. Eg: #hashtag1 #hashtag2 #hashtag3

### If you want to shuffle hashtags and multiply tweets
Please put hashtags in multiple lines inside hashtags.txt. Eg:
#hashtag1
#hashtag2
#hashtag3

***2 tweets + 7 hashtags will create 14 tweet posts in total***
