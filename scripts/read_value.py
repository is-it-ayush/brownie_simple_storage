from brownie import SimpleStorage, accounts, config

def read_contract():
    # print(SimpleStorage) | SimpleStorage is just an array of Contracts.
    # So whenever you deploy a contract on a real network or a test network. Brownie stores a reference to it in SimpleStorage array. [build/deployments/(chain_id)]
    # You can interact to it via SimpleStorage[0].
    simple_storage = SimpleStorage[-1] # -1 because we want to work with the most recent deployment. 
    print(simple_storage.retrieve())

def main():
    read_contract()