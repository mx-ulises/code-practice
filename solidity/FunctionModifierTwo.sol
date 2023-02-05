// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract FunctionModifierTwo {
    uint public total = 1000;
    bool public lock = false;

    // No Reentrancy modifier helps to lock a function while it is being executed.
    // It execute code between the lobs
    modifier noReentrancy() {
        require(lock == false, "No Reentrancy");
        lock = true;
        _;
        lock = false;
    }

    function substract(uint ammount) public noReentrancy {
        total -= ammount;
    }

    function badSubstract(uint ammount) public noReentrancy {
        if (0 < ammount) {
            total -= 1;
            badSubstract(ammount - 1);
        }
    }
}
