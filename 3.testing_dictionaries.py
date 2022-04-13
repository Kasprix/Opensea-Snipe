from collections import Counter
import pickle
import time


start_time = time.time()

with open('pickles/full_counter.pickle', 'rb') as handle:
    full_counter = pickle.load(handle)

with open('pickles/rarest_ten.pickle', 'rb') as handle:
    rarest_ten = pickle.load(handle)

with open('pickles/attribute_dictionary.pickle', 'rb') as handle:
    attribute_dictionary = pickle.load(handle)

rare_token_dict = {}

def countRareTokens(rarest_traits, attribute_dictionary): 
    rare_counter = 0 

    for value in attribute_dictionary:
        attribute_size = len(attribute_dictionary[str(value)])
        boolean_checker = False
        
        multiple_rares = 1
        for attribute_type in range(0,attribute_size):
            if str(attribute_dictionary[str(value)][attribute_type]) in dict(rarest_traits).keys():
                print(attribute_dictionary[value][attribute_type])
                boolean_checker = True
                multiple_rares += 1

        if boolean_checker == True:
            rare_counter += 1
            rare_token_dict[str(value)] = multiple_rares
            print('Rare:', multiple_rares)
        else: next
    print('Amount of rares counted: ' + str(rare_counter))


sorted_rare_tokens_list = {}

def getScore(token_id, attribute_ditionary, full_counter):
    print('------------------')
    attribute_size = len(attribute_ditionary[str(token_id)])
    rarity_score = 0 
    for v in range(0,attribute_size):
        print(attribute_ditionary[str(token_id)][v])
        rarity_score += full_counter[attribute_ditionary[str(token_id)][v]]
    sorted_rare_tokens_list[str(token_id)] = rarity_score
    print(rarity_score)

countRareTokens(rarest_ten, attribute_dictionary)

for value in rare_token_dict.keys():
    getScore(value, attribute_dictionary, full_counter)

counted_rarity_score = Counter(sorted_rare_tokens_list)
counted_rarity_score = counted_rarity_score.most_common()


with open('pickles/counted_rarity_score.pickle', 'wb') as handle:
    pickle.dump(counted_rarity_score, handle, protocol=pickle.HIGHEST_PROTOCOL)

print(counted_rarity_score)
print("--- %s seconds ---" % (time.time() - start_time))
