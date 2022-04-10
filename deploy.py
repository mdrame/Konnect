from dis import Bytecode
from itertools import chain
import json
from solcx import compile_standard, install_solc
import json
from web3 import Web3

with open("./Konnect.sol", "r") as file:
    simulatorStorageFile = file.read()
    # print(simulatorStorageFile)

# compiled smart contract using Py-solc-x
compiled_sol = compile_standard( 
    {
        "language": "Solidity",
        "sources": {"konnect.sol": {"content": simulatorStorageFile}},
        "settings": {
        "outputSelection": {
            "*": { "*" : ["abi", "metadata", "evm.Bytecode", "evm.sourceMap"] }
        }
    },
},
 
)
install_solc("0.6.0")
# print(compiled_sol)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# get byteCode
# ‼️ No byte after complied 
bytecode = compiled_sol["contracts"]["konnect.sol"]["BankAccountSimulator"]["evm"]["byte"]["object"]
# get abi
abi = compiled_sol["contracts"]["konnect.sol"]["BankAccountSimulator"]["abi"]
# for connecting to blockChain network / ganache
we = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
chain_id = 5777
my_address = "0x8d113377A76006bED975920FBfAe2d123E105a7B"
# Dummy key
private_key = "0x9fce1c2a0aba7eac7ed12c2d0abf88933af0112a4e8b8a83cea27cd5d3218689"

# create contract in python
SimulatorStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
# get latest transaction
nonce = web3.eth.getTransactionCount(my_address)
#build, sign & send transaction & wait
transaction = SimulatorStorage.constructor().buildTransaction (
    {"chainId": chain_id, "from": my_address, "nonce": nonce}
)
signed_txn = web3.eth.account.sign_transaction(transaction, private_key=private_key)
tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
tx_receipt = web3.eth.wait_for_transaction(signed_txn.rawTransaction)

