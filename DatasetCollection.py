#!/usr/bin/env python
# coding: utf-8

# In[27]:


import tweepy
import jsonpickle
import csv
import json
import time
st = time.time()


# In[20]:

auth = tweepy.AppAuthHandler(API_KEY,API_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
# where i save the tweets


# In[24]:


tweetsPerQuery = 100#this is the maximum provided by API
max_tweets = 100000000 # just for the sake of While loop
fName = r'G:\IIITD\Information Retrieval\Project\Shivani19128.github.io\tweet_data.txt'

since_id = None
max_id = -1
tweet_count = 0
print("Downloading the tweeets..takes some time..")


# In[25]:


search_query="#NRC"
x=0
with open(fName,'w') as f:
    print("Downloading hashtag" + search_query)
    while(tweet_count<max_tweets):
        try:
            if(max_id<=0):
                if(not since_id):
                    new_tweets = api.search(q=search_query,count=tweetsPerQuery,lang="en",tweet_mode='extended')

                else:
                    new_tweets = api.search(q=search_query,count=tweetsPerQuery,lang="en",tweet_mode='extended',since_id=since_id)
            else:
                if(not since_id):
                    new_tweets = api.search(q=search_query,count=tweetsPerQuery,lang="en",tweet_mode='extended',max_id=str(max_id-1))
                else:
                    new_tweets = api.search(q=search_query,count=tweetsPerQuery,lang="en",tweet_mode='extended',max_id=str(max_id-1),since_id=since_id)

            # Tweets Exhausted
            if(not new_tweets):
                print("No more tweets found!!")
                break
            # write all the new_tweets to a json file
            for tweet in new_tweets:
                f.write(jsonpickle.encode(tweet._json,unpicklable=False)+'\n')
                tweet_count+=len(new_tweets)
                print("Successfully downloaded {0} tweets".format(tweet_count))
                max_id=new_tweets[-1].id
        # in case of any error
        except tweepy.TweepError as e:
                print("Some error!!:"+str(e))
                break
end = time.time()

print("A total of {0} tweets are downloaded and saved to {1}".format(tweet_count,fName))
print("Total time taken is ",end-st,"seconds.")


# In[28]:


inputFile=r'G:\IIITD\Information Retrieval\Project\Shivani19128.github.io\tweet_data.txt'
tweets = []
for line in open(inputFile, 'r'):
    tweets.append(json.loads(line))
for tweet in tweets:
    try:
        csvWriter.writerow([tweet['full_text'],tweet['retweet_count'],tweet['user']['followers_count'],tweet['favorite_count'],tweet['place'],tweet['coordinates'],tweet['geo'],tweet['created_at'],str(tweet['id_str'])])
        count_lines+=1
    except Exception as e:
        print(e)


# In[3]:


import json
import csv


f = open('G:\IIITD\\Information Retrieval\\Project\\Shivani19128.github.io\\tweet_data.txt','a',encoding='utf-8')
csvWriter = csv.writer(f)
headers=['full_text','retweet_count','user_followers_count','favorite_count','place','coordinates','geo','created_at','id_str']
csvWriter.writerow(headers)

inputFile ="G:\\IIITD\\Information Retrieval\\Project\\Shivani19128.github.io\\tweet_data.txt"
tweets = []
for line in open(inputFile, 'r'):
    tweets.append(json.loads(line))

print('HI',len(tweets))
count_lines=0
for tweet in tweets:
    try:
        csvWriter.writerow([tweet['full_text'],tweet['retweet_count'],tweet['user']['followers_count'],tweet['favorite_count'],tweet['place'],tweet['coordinates'],tweet['geo'],tweet['created_at'],str(tweet['id_str'])])
        count_lines+=1
    except Exception as e:
        print(e)
print(count_lines)

# In[ ]:




