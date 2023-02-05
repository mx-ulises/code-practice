// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract FunctionModifierThree {
    uint LOWER_LIMIT = 100;
    uint public total = 1000;
    bool public lock = false;

    modifier noReentrancy() {
        require(lock == false, "No Reentrancy");
        lock = true;
        _;
        lock = false;
    }

    modifier lowerLimit(uint ammount) {
        require(LOWER_LIMIT <= total - ammount, "Invalid Witdraw");
        _;
    }

    // We can use more than one modifier at the time
    function substract(uint ammount) public noReentrancy lowerLimit(ammount) {
        total -= ammount;
    }
}
