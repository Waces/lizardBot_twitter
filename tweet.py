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


hourMin = 60
# 60 for Mins, 3600 for hours, 1 for seconds

# 90, 120 - 1h30m to 2h
# 60,90 - 1h to 1h30m

def poolRemove():
    texts.archived.append(txt)
    texts.text.remove(txt)

def poolReset():
    texts.text.extend(texts.archived)
    texts.archived.clear()


def tweet():
    api.update_with_media(im, txt)

# Main loop
while 1 == 1:
    sleepTime = random.randrange(3, 5)*hourMin
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
        scrapper.download() # Download one random image from Google
    except:
        print("Download Failed")
    scrapper.imn = len(os.listdir(path))+1
    imi = scrapper.imId			            # From here
    scrapper.imId = random.randrange(0, 101)
    if scrapper.imId == imi:
        scrapper.imId += 1                          
        if scrapper.imId > 100:
            scrapper.imId -= random.randrange(3, 6)
        elif scrapper.imId < 0:
            scrapper.imId -= random.randrange(3, 6) # To here is to make sure it doesn't pick the same, yeh, there are a lot better ways :P
    scrapper.downFile = scrapper.images[scrapper.imId]['ou']
    toRem = (path + "/" + random.choice(os.listdir(path))) # Select one random image to delete
    os.system("rm %s" %toRem) # Deletes the image
    print("Deleted:", toRem)
    print("---")
    time.sleep(sleepTime)
