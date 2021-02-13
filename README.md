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
- Change path variable to the directory of twitterBot-With-Selinum folder in your pc
- Fill up your twitter credentials inside configurations.py and save
- Prepare tweets in tweets.txt (folder: txt files)
- Prepare hashtags in hashtags.txt (folder: txt files)
- Open Command Prompt
- Type in the Command Prompt: cd the directory where twitter_ bot.py is. (Eg: cd C:\Users\user\Download\twitterBot-With-Selenium)
- Type python twitter_bot.py in Command Prompt

## To change tweet frequency
- Change the value of tweet_frequency variable inside configurations.py (line 19 of configurations.py)

### If you want to upload images in your tweet
While preparing your tweets in tweets.txt, please add "image prefix" of images you want to include in your tweet with "|". Eg: aaa|tweet1 - program will find all the images that include aaa and upload. Then post with "tweet1".

***Please note not to have similar names between images of different tweets. A good practice should be aaa1.jpg, aaa2.jpg for one tweet. Then bbb1.jpg, bbb2.jpg for another tweet.***

### If you do not want to upload images in your tweet
Just add "|" only in your tweets. Eg: |tweet2 - program will know no image to be uploaded and only post "tweet2".

### If you want to shuffle hashtags and multiply tweets
Please put hashtags in multiple lines inside hashtags.txt. Eg:<br/>
#hashtag1<br/>
#hashtag2<br/>
#hashtag3<br/>

### If you do not want to shuffle hashtags and multiply tweets
Please put hashtags in one line inside hashtags.txt. Eg:&nbsp;#hashtag1&nbsp;#hashtag2&nbsp;#hashtag3

***2 tweets + 7 hashtags will create 14 tweet posts in total***
