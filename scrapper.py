import json
import requests
import urllib.request
from bs4 import BeautifulSoup as bs

ua = [
    "User Agent" # Placeholder text
    ]

url = "Google Image Search URL" # Placeholder text

headers = {"User-Agent": ua }

req = requests.get(url, headers=headers)
html = req.content

soup = bs(html, "lxml")

images = soup.find_all("div", {"class": "rg_meta notranslate"})

images = [i.text for i in images]
images = [json.loads(i) for i in images]

#---
imId = 0 # Id of image to download

downFile = images[imId]['ou'] # url of the image to donwload
imn = 6 # Number of the file

# import pdb; pdb.set_trace()
# print(images[1]['ou'])
# urllib.request.urlretrieve(downFile, 'lizard')
# Here just test stuff

def download(): # Download
    urllib.request.urlretrieve(downFile, 'images/lizard%d' %imn )

