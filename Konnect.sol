pragma solidity ^0.6.0;

contract BankAccountSimulator {
    uint256 accountBalance = 10000;
    string bank = "BOF";
    uint256 accountNumber = 2747;

    function makeDeposite(uint256 amount) public {
        accountBalance += amount;
    }

    function makeWithdraw(uint256 amount) public {
        accountBalance -= amount;
    }

    function currentBalance() public view returns (uint256) {
        return accountBalance;
    }
}

contract simpleStorage {
    simpleStorage[] public simulatorChain;

    function processTransaction() public {
        simpleStorage newTransaction = new BankAccountSimulator();
        simulatorChain.push(newTransaction);
    }
}
