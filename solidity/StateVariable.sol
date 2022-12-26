// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract StateVariable {
    // We declare a State Variable that we will modify
    uint public num = 100;

    // We can override the value with a set transaction over the blockchain.
    function set(uint _num) public {
        num = _num;
    }

    // We can read the value from the blockchain without sending a transaction.
    function get() public view returns (uint) {
        return num;
    }
}
