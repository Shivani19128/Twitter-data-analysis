#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tweepy
import tqdm
import csv
import json
import time
from tqdm import tqdm_notebook as tqdm


# In[2]:


def makeAuthConnection():
    consumerApiKey = ''
    consumerApiSecret = ''
    acessToken = ''
    acessTokenSecret  = ''
    
    auth = tweepy.OAuthHandler(consumerApiKey, consumerApiSecret)
    #auth = tweepy.AppAuthHandler(consumerApiKey, consumerApiSecret)
    auth.set_access_token(acessToken, acessTokenSecret)
    
    return tweepy.API(auth , wait_on_rate_limit = True,wait_on_rate_limit_notify = True)


# In[3]:


api = makeAuthConnection()


# In[4]:


def checkRemainingSearchCount():
    jsonString = api.rate_limit_status()['resources']['search']['/search/tweets']
    upperLimit = jsonString['limit']
    remiaingFetch = jsonString['remaining']
    #resetTime = jsonString['reset']/60000 
    print (jsonString)
    return upperLimit, remiaingFetch


# In[5]:


checkRemainingSearchCount()


# In[6]:


def searchTweetsByHashtag(searchlist):
    
    searchFilter = ' AND -filter:links and -filter:videos'
    with open ("D:/Information Retrieval/Project/tweet_data.csv", "a", newline='', encoding="utf-8") as sampleFile:
        
        writer = csv.writer(sampleFile, quoting = csv.QUOTE_NONNUMERIC)
        try:
            for searchString in searchlist: 
                search_result = api.search(q=searchString + searchFilter, count=1, lang="en", tweet_mode='extended'
                                           , result_type  = 'recent')
                if(len(search_result) == 0):
                    print("*************No data on "+ searchString +" hashtag.***************")
                else : 
                    max_id = search_result[0].id
                    print("max_id",max_id)
                    old_id = -1
                    i = 1
                    while(max_id != old_id):
                        old_id = max_id
                        tweetDic = tweepy.Cursor(api.search,q = searchString + searchFilter  ,lang  = 'en'
                                                 ,include_entities=False,tweet_mode='extended',count = 100
                                                 ,max_id = max_id).items(300)
                        print("loop count",i)
                        for tweets in tweetDic:
                            jsonString = tweets._json
                            
                            csv_row = [jsonString['user']['location'], jsonString['place'], jsonString['retweet_count'], jsonString['created_at'],
                                       jsonString['full_text'].replace('\n', ' ')]  
                            
                            max_id = jsonString['id'] + 1
                            writer.writerow(csv_row)
                        print("Going to sleep to keep limit to check")    
                        time.sleep(3)
                        print("Waking Up")
                print("*************No more data to exact.*************")
        except tweepy.TweepError as e:
            print("Some error!!:"+str(e))


# In[7]:


search_criteria = ['#NRC','#CAA','#NPR']
searchTweetsByHashtag(search_criteria)


# In[ ]:




