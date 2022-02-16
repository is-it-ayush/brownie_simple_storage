import time
from brownie import accounts, config, SimpleStorage

def deploy_simple_storage():
    # account = accounts[0] | Fetch account from the temporary ganche local chain spin up while execution.
    # account = accounts.load("test_account") | Fetch account after adding it via "brownie accounts new test_account".
    # account = accounts.add(os.getenv("PRIVATE_KEY")) | Fetch account from .env (Remember to .gitignore).
    # account = accounts.add(config["wallets"]["from_key"]) | Fetch account from brownie-config.yaml.

    account = accounts[0]

    # Deploy the contract
    simple_storage = SimpleStorage.deploy({"from": account})

    # Call the retrieve function. We dont need {"from": account} aynmore since it's a view function. We aren't making any state change.
    stored_value = simple_storage.retrieve()
    print(stored_value)

    # It's again a transaction. We are making a state change to the chain. Hence we need to provide {"from": account} here.
    transaction = simple_storage.store(69, {"from": account})
    
    # Using this to prevent RPC Server Exception which generates the error: "Web3 is not connected."
    transaction.wait(1)
    
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)

    

def main():
    deploy_simple_storage()