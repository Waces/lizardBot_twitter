import tweepy
import time
from keys import keys
import texts
import random
import os

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

path = "images/"
im = ( path + "/" + random.choice(os.listdir(path)) )


hourMin = 60
# 60 for Mins, 3600 for hours, 1 for seconds


def poolRemove():
    texts.archived.append(txt)
    texts.text.remove(txt)

def poolReset():
    texts.text.extend(texts.archived)
    texts.archived.clear()
    #print('---')

def tweet():
    api.update_with_media(im, txt)

# Main loop
while 1 == 1:
    sleepTime = random.randrange(1, 5)*hourMin

    if len(texts.text) != 0:
        txt = random.choice(texts.text)
        poolRemove()
    else:
        poolReset()
        txt = random.choice(texts.text)
        poolRemove()
    #tweet()
    print(txt)
    time.sleep(sleepTime)