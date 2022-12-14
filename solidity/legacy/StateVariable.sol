// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract StateVariable {

    // This variable will store a number and can be queried without a transaction.
    uint public stateVariable;

    // Transaction to write the value.
    function set(uint _num) public {
        stateVariable = _num;
    }

    // Transaction to get the value, not needed as it can be queried directly.
    function get() public view returns (uint) {
        return stateVariable;
    }
}
