
# coding: utf-8

# In[20]:


import tweepy #most user friendly twitter API library

def build_model(tweets_categories):   
    
#STEP 1: Get global learning data set
#api connection to twitter
    CONSUMER_KEY= '####'
    CONSUMER_SECRET = '####'
    ACCESS_KEY = '####'
    ACCESS_SECRET = '####'
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)


#Use tweepy Cursor to get all tweets relating to a query in the english language
    for tweet in tweepy.Cursor(api.search, q=tweets_categories,count=1,result_type="recent",include_entities=True, lang="en").items(5):
        tweeties= tweet.text
    return tweeties


# In[19]:


build_model('car')


# In[ ]:




