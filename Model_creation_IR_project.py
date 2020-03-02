#!/usr/bin/env python
# coding: utf-8

# In[4]:


from textblob.classifiers import NaiveBayesClassifier
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

#Model Selection and Validation
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix, classification_report,accuracy_score
from textblob import TextBlob
from textblob import Word


# In[5]:


def read_dataset():
    df = pd.read_excel(r"G:\\IIITD\\Information Retrieval\\Project\\Shivani19128.github.io\\Harshita.xlsx")
    column = df.columns
    data = df['Tweet']
    print(type(data))
    tweets = data.values.tolist()
    return tweets
tweets = read_dataset()


# In[6]:


def sentiment_analysis(tweets):
    polarity = []
    subjectivity = []
    for i in range(len(tweets)):
        text = tweets[i]
        #print(i, type(text))
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


# In[ ]:





# In[7]:


#Calculate % of positive, neutral and negative sentiment
def polarity_count(polarity):
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
    print("% of positive tweets: ",pos)
    print("% of negative tweets: ",neg)
    print("% of neutral tweets: ",neutral)
    return pos,neg,neutral
pos,neg,neutral = polarity_count(polarity)


# In[8]:


def add_column(polarity,subjectivity):
    df = pd.read_excel(r"G:\\IIITD\\Information Retrieval\\Project\\Shivani19128.github.io\\Harshita.xlsx")
    df = df.assign(polarity_score=polarity)
    tweets = df.assign(subjectivity_score = subjectivity)
    print(tweets.head(5))
    return tweets
tweets = add_column(polarity,subjectivity)


# In[10]:


def model():
    pipeline = Pipeline([
        ('bow',CountVectorizer()),  # strings to token integer counts
        ('tfidf', TfidfTransformer()),  # integer counts to weighted TF-IDF scores
        ('classifier', MultinomialNB()),  # train on TF-IDF vectors w/ Naive Bayes classifier
    ])
    msg_train, msg_test, label_train, label_test = train_test_split(tweets['Tweet'], tweets['polarity_score'], test_size=0.2)
    pipeline.fit(msg_train,label_train)
    predictions = pipeline.predict(msg_test)
    print(classification_report(predictions,label_test))
    print(confusion_matrix(predictions,label_test))
    print(accuracy_score(predictions,label_test))
model()


# In[15]:


d1 = pd.DataFrame(polarity)
d1 = d1.replace(to_replace =[0],value= 'Neutral')
d1 = d1.replace(to_replace =[1],value= 'Positive')
d1 = d1.replace(to_replace =[-1],value= 'Negative')


# In[20]:


import seaborn as sns
sns.set(style='darkgrid')
ax = sns.countplot(x=0,data=d1)


# In[ ]:




