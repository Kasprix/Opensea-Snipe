import requests
import time
import random
import collections
import pickle


start_time = time.time()

# Ethalien
TOTAL_SUPPLY =  2200
BASE_URL = f"https://kibatsumecha.com/api/metadata/"
valueList = []

s = requests.Session()

# with session 8.741260
# no sesh 25.24572

# At 200: 31 seconds
# 87,88 Traits

# At 300: 47,50 seconds
# 86,85 Traits

# At 500: 77,77 seconds
# 90,89 Traits

def fetch(session, url):
    with session.get(url) as response:
        return response.json()

for i in random.sample(range(1, TOTAL_SUPPLY), 1200):
    URL = BASE_URL + str(i)
    page = fetch(s, URL)

    count = len(page['attributes'])

    for v in range(0,count):
        print(page['attributes'][v]['value'])
        valueList.append(page['attributes'][v]['value'])


counter=collections.Counter(valueList)



print(counter)
print(len(counter))

with open('counter.pickle', 'wb') as outputfile:
    pickle.dump(counter, outputfile)

print("--- %s seconds ---" % (time.time() - start_time))
