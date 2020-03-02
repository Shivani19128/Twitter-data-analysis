#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tweepy
import jsonpickle
import csv
import json
import time
st = time.time()


# In[2]:


API_KEY="U4wOpovGp6q0Qwh6hlKw73DXS"
API_SECRET="kswr8NidjxveJvLyCl8ZXsVz5xdckJkNhGbGd1pjxgIz1v5zWa"
ACCESS_TOKEN="1221825061184659457-GQAQH2lt7HhI23ihIJ81NzLHZUTtAY"
ACCESS_TOKEN_SECRET="yw69GXrZWnIAFyetKOEnFve2DIpfQHxQ9L73gghJkAXdw"

auth = tweepy.AppAuthHandler(API_KEY,API_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
# where i save the tweets


# In[3]:


tweetsPerQuery = 100#this is the maximum provided by API
max_tweets = 10000 # just for the sake of While loop
fName = r'G:\IIITD\Information Retrieval\Project\Shivani19128.github.io\tweet_data.txt'

since_id = None
max_id = -1
tweet_count = 0
print("Downloading the tweeets..takes some time..")


# In[4]:


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


# In[6]:


f = open('G:\\IIITD\\Information Retrieval\\Project\\Shivani19128.github.io\\harshita_data.csv','a',encoding='utf-8')
csvWriter = csv.writer(f)
headers=['full_text','retweet_count','user_followers_count','favorite_count','place','coordinates','geo','created_at','id_str','location']
csvWriter.writerow(headers)

inputFile ="G:\\IIITD\\Information Retrieval\\Project\\Shivani19128.github.io\\tweet_data.txt"
tweets = []
for line in open(inputFile, 'r'):
    tweets.append(json.loads(line))

print('HI',len(tweets))
count_lines=0
for tweet in tweets:
    try:
        csvWriter.writerow([tweet['full_text'],tweet['retweet_count'],tweet['user']['followers_count'],tweet['favorite_count'],tweet['place'],tweet['coordinates'],tweet['geo'],tweet['created_at'],str(tweet['id_str']),tweet['user']['location']])
        count_lines+=1
    except Exception as e:
        print(e)
print(count_lines)


# In[118]:


from textblob import TextBlob
from textblob import Word


# In[124]:


w = Word("")
w.lemmatize()


# In[126]:





# In[117]:


def translate_language(tweets):
    for text in tweets:
        print(text)
        wiki = TextBlob(text)
        lang = wiki.detect_language()
        print(lang)
        if lang=='hi':
            wiki = wiki.translate(from_lang='en',to='hi')
            print(wiki)
            wiki = wiki.translate(to='en')
        elif lang!='en':
            wiki = wiki.translate(to='en')
        print(wiki)
tweets = ["bhai sahab","bhai sahab What is waiting for","RT Dear Bhai After #NRC and deporting illegals Aadhaar should only be the India ID and should be linked to Vot"] 
translate_language(tweets)


# In[133]:


wiki = TextBlob("bhai sahab")
#wiki = wiki.translate(to='en')


# In[134]:


wiki = wiki.translate(from_lang='en',to='hi')
print(wiki)
wiki = wiki.translate(to='en')
print(wiki)
#print(wiki.correct())


# In[180]:


from textblob.classifiers import NaiveBayesClassifier
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

#Model Selection and Validation
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix, classification_report,accuracy_score


# In[181]:


df = pd.read_excel(r"G:\\IIITD\\Information Retrieval\\Project\\Shivani19128.github.io\\Harshita.xlsx")
#print(df.head(5))
column = df.columns
data = df['Tweet']
print(data)


# In[182]:


print(type(data))
tweets = data.values.tolist()
print(type(tweets[1558]))


# In[183]:


def sentiment_analysis(tweets):
    polarity = []
    subjectivity = []
    for i in range(len(tweets)):
        text = tweets[i]
        print(i, type(text))
        text_sentiment = TextBlob(text)
        if text_sentiment.sentiment.polarity>0:
            polarity.append(1)
        elif text_sentiment.sentiment.polarity==0:
            polarity.append(0)
        else:
            polarity.append(-1)
        if text_sentiment.sentiment.subjectivity>=0.5:
            subjectivity.append(1)
        else:
            subjectivity.append(0)
    print(len(polarity))
    print(len(subjectivity))
    return polarity,subjectivity
polarity, subjectivity = sentiment_analysis(tweets)    
print(type(polarity))


# In[184]:


#Calculate % of positive, neutral and negative sentiment
pos = 0
neg = 0
neutral = 0
for score in polarity:
    if score==1:
        pos+=1
    elif score==-1:
        neg+=1
    else:
        neutral+=1
pos = ((pos/len(polarity))*100)
neg = ((neg/len(polarity))*100)
neutral = ((neutral/len(polarity))*100)
print(pos,neg,neutral)


# In[185]:


df = df.assign(polarity_score=polarity)
train_tweets = df.assign(subjectivity_score = subjectivity)
print(train_tweets.head(5))


# In[ ]:





# In[186]:


pipeline = Pipeline([
    ('bow',CountVectorizer()),  # strings to token integer counts
    ('tfidf', TfidfTransformer()),  # integer counts to weighted TF-IDF scores
    ('classifier', MultinomialNB()),  # train on TF-IDF vectors w/ Naive Bayes classifier
])


# In[187]:


msg_train, msg_test, label_train, label_test = train_test_split(train_tweets['Tweet'], train_tweets['polarity_score'], test_size=0.2)
pipeline.fit(msg_train,label_train)
predictions = pipeline.predict(msg_test)
print(classification_report(predictions,label_test))
print(confusion_matrix(predictions,label_test))
print(accuracy_score(predictions,label_test))


# In[ ]:




