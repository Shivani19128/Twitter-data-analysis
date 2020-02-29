#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import emoji
import numpy as np


# In[20]:


Data = pd.read_excel("D:/Information Retrieval/Project/Vineet.xlsx")
print(Data.shape)
print(Data.columns)


# In[21]:


Data.drop_duplicates(subset ="Tweets",keep = False, inplace = True)
print(Data.shape)


# In[22]:


Data.to_csv("D:/Information Retrieval/Project/Unique_Tweet_Data.csv")


# In[23]:


emojis = ["\U0001F600","\U0001F603","\U0001F604","\U0001F601","\U0001F606","\U0001F605","\U0001F923","\U0001F602","\U0001F642",
          "\U0001F643","\U0001F609","\U0001F60A","\U0001F607","\U0001F970","\U0001F60D","\U0001F929", "\U0001F618" "\U0001F617",
          "\U0001F61A","\U0001F619","\U0001F60B","\U0001F61B","\U0001F61C","\U0001F92A","\U0001F61D","\U0001F911","\U0001F917",
         "\U0001F92D","\U0001F92B","\U0001F914","\U0001F910","\U0001F928","\U0001F610","\U0001F611","\U0001F636","\U00001F60F",
          "\U0001F612","\U0001F644","\U0001F62C","\U0001F925","\U0001F60C","\U0001F614","\U0001F62A","\U0001F924","\U0001F634",
          "\U0001F637","\U0001F912","\U0001F915","\U0001F922"]


# In[24]:


print(type(Data))


# In[25]:


for k in range(3):
    
    x = Data.iloc[k,3]
    words = x.split()
    for word in words:
        if(word[0] == "@"):
            Data.iloc[k,3] = Data.iloc[k, 3].replace(word, "")
    
for k in range(3):
    print(Data.iloc[k,3],"\n")


# In[28]:


special_characters = {
    "â‚¬":"€", "â€š":"‚", "â€ž":"„", "â€¦":"…", "Ë†":"ˆ","â€¹":"‹", "â€˜":"‘", "â€™":"’", "â€œ":"“", "â€":"”",
    "â€¢":"•", "â€“":"–", "â€”":"—", "Ëœ":"˜", "â„¢":"™","â€º":"›", "Å“":"œ", "Å’":"Œ", "Å¾":"ž", "Å¸":"Ÿ","Å¡":"š",
    "Å½":"Ž", "Â¡":"¡", "Â¢":"¢", "Â£":"£","Â¤":"¤", "Â¥":"¥", "Â¦":"¦", "Â§":"§", "Â¨":"¨","Â©":"©", "Âª":"ª", 
    "Â«":"«", "Â¬":"¬", "Â®":"®","Â¯":"¯", "Â°":"°", "Â±":"±", "Â²":"²", "Â³":"³","Â´":"´", "Âµ":"µ", "Â¶":"¶",
    "Â·":"·", "Â¸":"¸","Â¹":"¹", "Âº":"º", "Â»":"»", "Â¼":"¼", "Â½":"½","Â¾":"¾", "Â¿":"¿", "Ã€":"À", "Ã‚":"Â",
    "Ãƒ":"Ã","Ã„":"Ä", "Ã…":"Å", "Ã†":"Æ", "Ã‡":"Ç", "Ãˆ":"È","Ã‰":"É", "ÃŠ":"Ê", "Ã‹":"Ë", "ÃŒ":"Ì", "ÃŽ":"Î",
    "Ã‘":"Ñ", "Ã’":"Ò", "Ã“":"Ó", "Ã”":"Ô", "Ã•":"Õ","Ã–":"Ö", "Ã—":"×", "Ã˜":"Ø", "Ã™":"Ù", "Ãš":"Ú","Ã›":"Û", 
    "Ãœ":"Ü", "Ãž":"Þ", "ÃŸ":"ß", "Ã¡":"á","Ã¢":"â", "Ã£":"ã", "Ã¤":"ä", "Ã¥":"å", "Ã¦":"æ","Ã§":"ç", "Ã¨":"è",
    "Ã©":"é", "Ãª":"ê", "Ã«":"ë","Ã¬":"ì", "Ã­":"í", "Ã®":"î", "Ã¯":"ï", "Ã°":"ð","Ã±":"ñ", "Ã²":"ò", "Ã³":"ó",
    "Ã´":"ô", "Ãµ":"õ","Ã¶":"ö", "Ã·":"÷", "Ã¸":"ø", "Ã¹":"ù", "Ãº":"ú","Ã»":"û", "Ã¼":"ü", "Ã½":"ý", "Ã¾":"þ", "Ã¿":"ÿ"
  }


# In[60]:


for k in range(1):
    
    x = Data.iloc[k,3]
    print(type(Data.iloc[k,3]))
    words = x.split()
    for i in range(len(words)):
    
        word = words[i] 
        for k in special_characters:
            if(k in word):
                print(k)
                print(word,"\n")
                word = word.replace(k,special_characters[k])
                print(word)
                words[i] = word
    
    print(type(words))
    listToStr = ' '.join([str(elem) for elem in words])
    print(type(listToStr))
    Data.iloc[k,3] = listToStr 


# In[ ]:




