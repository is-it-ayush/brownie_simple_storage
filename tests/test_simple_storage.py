from cmath import exp
from brownie import SimpleStorage, accounts,network

# Some Useful Tips:
# - If you want to only run one test in brownie. Use "brownie test -k name_of_test_function"
# - If you want to launch a Python shell just to verify things yourself. Use "brownie test --pdb"
# - If you want to be detailed about which test failed. Use "brownie test -s"
# Bronwie test is equivalent to the python package "pytest"

def test_deploy():
    # Intialize
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": get_account()})
    initial_value = simple_storage.retrieve()
    expected_value = 0
    # Assert (Its a keyword basically used to check certain conditions and raises error if not met.)
    assert initial_value == expected_value, "The initial value is not equal to expected value!"
    
def test_updating_storage():
    # Intialize
    simple_storage = SimpleStorage.deploy({"from": get_account()})
    # Act (Since we are making a state change, it would be a transaction.)
    expected_value = 69
    simple_storage.store(expected_value, {"from": get_account()})
    # Assert
    assert simple_storage.retrieve() == expected_value, "The updated value is not equal to expected value!"


# Helper Functions

def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.load("test_account")