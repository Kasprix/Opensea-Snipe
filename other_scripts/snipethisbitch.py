import pickle
import requests
import time



start_time = time.time()


# Loads up Big probability pickle
with open('counter.pickle', 'rb') as inputfile:
    counter = pickle.load(inputfile)

# Loads up Big probability pickle
with open('lowestBuys.pickle', 'rb') as inputfile:
    snipeItems = pickle.load(inputfile)


SnipeDics = {}


s = requests.Session()

BASE_URL = f"https://kibatsumecha.com/api/metadata/"

for i in snipeItems:
    print('---------')
    #print(str(i).strip("[]'"))
    #print('')
    URL = BASE_URL + str(i).strip("[]'")
    page = s.get(URL)
    page = page.json()

    count = len(page['attributes'])


    MIN_VALUE = 100000

    for v in range(0,count):

        if page['attributes'][v]['value'] in counter:
            #if page['attributes'][v]['value'] <= MIN_VALUE:
                number = page['attributes'][v]['value']
                if counter[number] <= MIN_VALUE:
                    #print(page['attributes'][v]['value'])
                    #print(counter[number])
                    MIN_VALUE = counter[number]
                    MIN_NAME = page['attributes'][v]['value']
                # print(page['attributes'][v]['value'])
                else:
                    next
        else:
            next
                #valueList.append(page['attributes'][v]['value'])
    #print(MIN_NAME)
    #print(MIN_VALUE)
    SnipeDics[str(i).strip("[]'")] = MIN_VALUE
    #print('---------')
print (dict(sorted(SnipeDics.items(), key=lambda item: item[1])))

print("--- %s seconds ---" % (time.time() - start_time))

