from concurrent.futures import ThreadPoolExecutor
import time
import requests
import collections
import pickle
from contractVariables import TOTAL_SUPPLY

with open('pickles/baseURI.pickle', 'rb') as handle:
    URL = pickle.load(handle)

valueList = []
attribute_dictionary = {}
counter = 0

def fetch(session, url, token_id):
    sesh_url = url + str(token_id)
    with session.get(sesh_url) as response:
        count = len(response.json()['attributes'])
        attribute_dictionary[str(token_id)] = {}

        for v in range(0,count):
            value = response.json()['attributes'][v]['value']
            print(response.json()['attributes'][v]['value'])
            valueList.append(response.json()['attributes'][v]['value'])
            attribute_dictionary[str(token_id)][v] = value
    return response.json()


def main():
    start_time = time.time()
    with ThreadPoolExecutor(max_workers = 100 ) as executor:
            with requests.Session() as session:
                # Time at session = 100, max_workers = 100: 142 Seconds, 86 Seconds, 107 Seconds
                # Time at session = 200, max_workers = 200: 130 Seconds, 114 Seconds, 96 Seconds
                [executor.map(fetch, [session] * 200, [URL], [str(i)]) for i in range(1, TOTAL_SUPPLY-1)]
                executor.shutdown(wait=True)


    counter = collections.Counter(valueList)

    rarest_ten = counter.most_common()[:-18:-1]

    with open('pickles/full_counter.pickle', 'wb') as handle:
        pickle.dump(counter, handle, protocol=pickle.HIGHEST_PROTOCOL)

    with open('pickles/rarest_ten.pickle', 'wb') as handle:
        pickle.dump(rarest_ten, handle, protocol=pickle.HIGHEST_PROTOCOL)

    with open('pickles/attribute_dictionary.pickle', 'wb') as handle:
        pickle.dump(attribute_dictionary, handle, protocol=pickle.HIGHEST_PROTOCOL)

    
    print('------------------')   
    print(rarest_ten)
    print("--- %s seconds ---" % (time.time() - start_time))

main()