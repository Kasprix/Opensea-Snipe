import requests
import contractVariables
import time
import pickle
import operator

start_time = time.time()

with open('pickles/counted_rarity_score.pickle', 'rb') as handle:
    counted_rarity_score = pickle.load(handle)

with open('pickles/baseURI.pickle', 'rb') as handle:
    baseURI = pickle.load(handle)

contractAddress = contractVariables.contract_address

listed_items = {}
listed_items_rank = {}

def apiCall(contractAddress, token_id, rank):
    url = "https://api.opensea.io/api/v1/asset/" + contractAddress + "/" + str(token_id) + "/listings?limit=20"

    headers = {
        "Accept": "application/json",
        "X-API-KEY": "6f04961485d14e4585edd096fda589d4"
    }
    
    response = requests.request("GET", url, headers=headers)
    
    try:
        if len(response.json()['listings']) == 0:
            print('Fail')
            next
        else:
            price = float(response.json()['listings'][0]['base_price'])/(10**18)
            print('Success')
            print('Token ID:', token_id)
            listed_items[str(token_id)] = price
            listed_items_rank[str(token_id)] = rank
    except KeyError:
        next

for item in counted_rarity_score:
    apiCall(contractAddress, item[0], item[1])


sorted_listed_items = dict(sorted(listed_items.items(), key=operator.itemgetter(1), reverse=True))
sorted_listed_items_rank = dict(sorted(listed_items_rank.items(), key=operator.itemgetter(1), reverse=True))

ranked = {key: rank for key, rank in enumerate(sorted(listed_items_rank, key=listed_items_rank.get, reverse=False), 1)}

for v in sorted_listed_items:
    print('------------------')
    print('Token ID:', v)
    print('Price:', sorted_listed_items[v])
    print('Rank:', list(ranked.keys())[list(ranked.values()).index(v)])
    print('Score:', sorted_listed_items_rank[v])
    print('OS Link: https://opensea.io/assets/' + contractAddress + '/' + str(v))
    print('Metadata Link: ' + baseURI + str(v))

print(sorted_listed_items_rank)
print("--- %s seconds ---" % (time.time() - start_time))
