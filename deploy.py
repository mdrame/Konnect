from dis import Bytecode
from solcx import compile_standard, install_solc

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
print(compiled_sol)
