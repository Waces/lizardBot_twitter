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
im = ( path + "/" + random.choice(os.listdir(path)) ) # Random image [wip?]


hourMin = 60
# 60 Mins, 3600 hours, 1 seconds


def poolRemove(): # Remove/Move from the 'not used' text list to 'used' text list
    texts.archived.append(txt)
    texts.text.remove(txt)

def poolReset(): # When 'non used' text list is empty, will get again the the lines from the 'used' list
    texts.text.extend(texts.archived)
    texts.archived.clear()
    #print('---')

def tweet():
    api.update_with_media(im, txt)

# Main loop
while 1 == 1:
    sleepTime = random.randrange(1, 5)*hourMin # 'Loop time' range

    if len(texts.text) != 0: # Only pick text if list is not empty
        txt = random.choice(texts.text) # Pick random text from 'not used' text list
        poolRemove()
    else:
        poolReset()
        txt = random.choice(texts.text)
        poolRemove()
    # tweet()
    print(txt) # Just for the sake of debugging 
    time.sleep(sleepTime) # Loop 'timer'
