import tweepy
import time
from keys import keys
import texts
import scrapper
import random
import os

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

path = "images"


hourMin = 3600
# 60 for Mins, 3600 for hours, 1 for seconds

# 90, 120 - 1h30m to 2h
# 60,90 - 1h to 1h30m
# 6, 10 (3600) to 6 to 12h

def poolRemove():
    texts.archived.append(txt)
    texts.text.remove(txt)

def poolReset():
    texts.text.extend(texts.archived)
    texts.archived.clear()
    # print('---')

def tweet():
    api.update_with_media(im, txt)

def errorTweet():
    api.update_status('@Waces_Ferpit, BOT CRASHED! Please come to see the console.')

# Main loop
while 1 == 1:
    sleepTime = random.randrange(6, 12)*hourMin
    im = (path + "/" + random.choice(os.listdir(path)))

    if len(texts.text) != 0:
        txt = random.choice(texts.text)
        poolRemove()
    else:
        poolReset()
        txt = random.choice(texts.text)
        poolRemove()
    tweet()
    print("Text:",txt)  # Just for the sake of debugging
    print("Image:", im)
    print("Downloaded:", scrapper.downFile)

    # print("---")
    try:
        scrapper.download()
    except:
        print("Download Failed")
    scrapper.imn = len(os.listdir(path))+1
    imi = scrapper.imId
    scrapper.imId = random.randrange(0, 101)
    if scrapper.imId == imi:
        scrapper.imId += 1
        if scrapper.imId > 100:
            scrapper.imId -= random.randrange(3, 6)
        elif scrapper.imId < 0:
            scrapper.imId -= random.randrange(3, 6)
    scrapper.downFile = scrapper.images[scrapper.imId]['ou']
    toRem = (path + "/" + random.choice(os.listdir(path)))
    os.system("rm %s" %toRem)
    print("Deleted:", toRem)
    print("---")
    time.sleep(sleepTime)

errorTweet() #Tweet me ( @Waces_Ferpit ) if main loop breaks or anything.
