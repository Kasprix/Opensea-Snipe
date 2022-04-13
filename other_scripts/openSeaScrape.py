import cloudscraper
from bs4 import BeautifulSoup
import json
import pickle
import time
import re
import requests


# 2.7 Seconds
start_time = time.time()


s = requests.Session()


scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
# Or: scraper = cloudscraper.CloudScraper()  # CloudScraper inherits from requests.Session
#print (scraper.get("https://opensea.io/collection/dystopunks-vx?search[sortBy]=PRICE&search[sortAscending]=true&search[toggles][0]=BUY_NOW").text)  # => "<!DOCTYPE html><html><head>..."

COLLECTION_SLUG = 'kibatsu-mecha'

lynx = scraper.get("https://opensea.io/collection/" + COLLECTION_SLUG + "?search[sortBy]=PRICE&search[sortAscending]=true&search[toggles][0]=BUY_NOW").text

numbers = re.compile(r'\d+(?:\.\d+)?')

r1 = re.findall(r'tokenId.......',lynx)

values = []

for v in r1:
    values.append(numbers.findall(v))

values = list(filter(None, values))

with open('lowestBuys.pickle', 'wb') as outputfile:
    pickle.dump(values, outputfile)

print(str(values[0]).strip("[]'"))

print("--- %s seconds ---" % (time.time() - start_time))
