
import string
import requests
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import json
import re
import pandas as pd 
from datetime import datetime, timedelta 
import pandas as pd 

column_name = ["users_name","num_followers","num_tracks", "users_link"]

class Crawler():
    def __init__(self) -> None:
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        self.driver = webdriver.Chrome(service=Service(
            ChromeDriverManager().install()),options=chrome_options)

        self.data = {}

    def generator_result_columns(self,column_name=None):
        for name in column_name:
              self.data[name] = []
        return self.data
    
    # Ham lay thong tin users bang keyword

    def get_info_users(self, keyword):
        
        url = f'https://soundcloud.com/search/people?q={keyword}'
        
        self.driver.get(url)
        
        for i in range(0,50):
            
            time.sleep(1)
        
            self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        
        time.sleep(1)
        
        page_source = self.driver.page_source
        
        soup = BeautifulSoup(page_source, 'html.parser')
        
        data_list = soup.find_all('li', class_='searchList__item')
        
        for i in data_list:
            
            name = i.find('a', class_='sc-link-dark sc-link-primary')
            
            follower_track = i.find_all('span', class_='sc-visuallyhidden')
            
            if(follower_track == []):
                self.data["num_followers"].append('0')
                self.data["num_tracks"].append('0')
            elif (len(follower_track)==1):
                if('track' in follower_track[0]):
                    self.data["num_tracks"].append(follower_track[1].text)
                    self.data["num_followers"].append('0')
                else:
                    self.data["num_followers"].append(follower_track[0].text)
                    self.data["num_tracks"].append('0')
            else:
                self.data["num_tracks"].append(follower_track[1].text)
                self.data["num_followers"].append(follower_track[0].text)
                
            profile_link = name.get('href')
            
            link = 'https://soundcloud.com' + profile_link
            
            self.data["users_name"].append(name.text)
            
            self.data["users_link"].append(link)

            if(len(self.data["users_name"])==50):
                return self.data
            
    def save(self):
        df = pd.DataFrame(self.data)
        df.to_csv("./data/Soundcloud_User.csv", index=True)


        

