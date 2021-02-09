from selenium import webdriver #pip install selenium
from selenium import common
from selenium.webdriver.common import keys #pip install webdriver-manager
from webdriver_manager.chrome import ChromeDriverManager
import subprocess
import time
import os

import configurations
#import bot file name
filename = configurations.bot_file

# Twitter credentials
twitter_name = configurations.username
twitter_pass = configurations.password

class Twitter_Service(object):

    def __init__(self):
        pass

    # Senitise User Input
    def sanitised_input(self, prompt, type_=None, min_=None, max_=None, range_=None):
        if min_ is not None and max_ is not None and max_ < min_:
            raise ValueError("min_ must be less than or equal to max_.")
        while True:
            ui = input(prompt)
            if type_ is not None:
                try:
                    ui = type_(ui)
                except ValueError:
                    print("Input type must be {0}.".format(type_.__name__))
                    continue
            if max_ is not None and ui > max_:
                print("Input must be less than or equal to {0}.".format(max_))
            elif min_ is not None and ui < min_:
                print("Input must be greater than or equal to {0}.".format(min_))
            elif range_ is not None and ui not in range_:
                if isinstance(range_, range):
                    template = "Input must be between {0.start} and {0.stop}."
                    print(template.format(range_))
                else:
                    template = "Input must be {0}."
                    if len(range_) == 1:
                        print(template.format(*range_))
                    else:
                        expected = " or ".join((
                            ", ".join(str(x) for x in range_[:-1]),
                            str(range_[-1])
                        ))
                        print(template.format(expected))
            else:
                return ui

    # Read data from file
    def read_file(self, filename):
        with open(filename) as fin:
            data = fin.read().splitlines(True)
            data_count = len(data)

            if (data_count==0):
                return {
                    "have_data" : False,
                }  

            else:
               return {
                    "have_data" : True,
                    "data" : data,
                }
    
    # Write data to file
    def write_file(self, filename, data):
        with open(filename, 'w') as fout:
                fout.writelines(data)
        return True

    # Combine and rotate hashtags
    def rotate_hashtags(self, list_input, n):
        rotated_list = list_input[n:] + list_input[:n]
        rotated_hashtag_string = ""
        
        for item in rotated_list:
            rotated_hashtag_string += " " + item
        
        return rotated_hashtag_string

    # Initiate browser
    def initiate_browser(self):
        browser  = webdriver.Chrome(ChromeDriverManager().install())
        time.sleep(3)
        return browser

    # Open Twitter Website
    def open_twitter(self, browser):
        browser.get('https://twitter.com/login/')
        time.sleep(3)

    # Fill credentials and login
    def login(self, browser):
        try:
            browser.find_element_by_name('session[username_or_email]').send_keys(twitter_name)
            time.sleep(1)
            browser.find_element_by_name('session[password]').send_keys(twitter_pass)
            time.sleep(1)
            browser.find_element_by_name('session[password]').send_keys(keys.Keys.RETURN)
            time.sleep(3)
    
        except Exception as e:
            print("EXCEPTION - LOG IN. RESTARTING!")
            print(e)
            time.sleep(2)
            browser.close()
            time.sleep(2)
            subprocess.Popen('python ' + filename, shell=True).wait()

    # Logout
    def logout(self, browser):
        try:
            browser.find_element_by_xpath("//div[@data-testid='SideNav_AccountSwitcher_Button']").click()
            time.sleep(2)
            browser.find_element_by_xpath("//a[@data-testid='AccountSwitcher_Logout_Button']").click()
            time.sleep(2)
            browser.find_element_by_xpath("//div[@data-testid='confirmationSheetConfirm']").click()
            time.sleep(3)
            
        except Exception as e:
            print("EXCEPTION - LOG OUT. RESTARTING!")
            print(e)
            time.sleep(2)
            browser.close()
            time.sleep(2)
            subprocess.Popen('python ' + filename, shell=True).wait()

    # Post tweets
    def post_tweets(self, browser, hashtagged_tweets):
        tweet = hashtagged_tweets[0]

        try:
            browser.find_element_by_xpath("//a[@data-testid='SideNav_NewTweet_Button']").click()
            time.sleep(2)

            img = tweet.split('|')[0]
            tweet = tweet.split('|')[1]

            if(img!=''):
                files = []
                for i in os.listdir(configurations.img_path):
                    if os.path.isfile(os.path.join(configurations.img_path,i)) and img in i:
                        files.append(i)
                
                for file_ in files:
                    file_upload = browser.find_element_by_xpath("//input[@type='file']")
                    browser.execute_script("arguments[0].style.display = 'block';", file_upload)
                    file_upload.send_keys(configurations.img_path + file_)

            browser.find_element_by_xpath("//div[@role='textbox']").send_keys(tweet)
            time.sleep(2)
            browser.find_element_by_class_name("notranslate").send_keys(keys.Keys.ENTER)
            time.sleep(2)
            browser.find_element_by_xpath("//div[@data-testid='tweetButton']").click()
            time.sleep(3)
        
        except Exception as e:
            print("EXCEPTION - POST TWEETS. RESTARTING!")
            print(e)
            time.sleep(2)
            browser.close()
            time.sleep(2)
            subprocess.Popen('python ' + filename, shell=True).wait()

    # Search tweets
    def search_tweets(self, browser, keyword):
        try:
            browser.get('https://twitter.com/hashtag/' + keyword + '?src=hashtag_click')
            return True

        except Exception as e:
            print("EXCEPTION - SEARCH TWEETS. RESTARTING!")
            print(e)
            time.sleep(2)
            browser.close()
            time.sleep(2)
            subprocess.Popen('python ' + filename, shell=True).wait()