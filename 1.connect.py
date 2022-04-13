from web3 import Web3
import contractVariables
import time
import pickle

def checkBaseURI(): 
    start_time = time.time()

    infura_url = 'https://mainnet.infura.io/v3/672df4fc8ba147609c2c71cade0b449f'
    web3 = Web3(Web3.HTTPProvider(infura_url))

    contract_instance = web3.eth.contract(address=contractVariables.contract_address, abi=contractVariables.contract_ABI)

    unrevealedURI = str(contract_instance.functions.tokenURI(1).call())[:-1]

    while str(contract_instance.functions.tokenURI(1).call())[:-1] == unrevealedURI:
        print('still the same')
        time.sleep(10)

    baseURI = str(contract_instance.functions.tokenURI(1).call())[:-1]

    if 'ipfs://' in baseURI:

        baseURI = 'https://ipfs.io/ipfs/' + baseURI.split("ipfs://",1)[1]
        print(baseURI)

    else: next

    with open('pickles/baseURI.pickle', 'wb') as handle:
        pickle.dump(baseURI, handle, protocol=pickle.HIGHEST_PROTOCOL)

    print("--- %s seconds ---" % (time.time() - start_time))

    return baseURI
        
base = checkBaseURI()
