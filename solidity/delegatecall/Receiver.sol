// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

// This contract should be deployed first
contract Receiver {
    // Storage must be the same as in Caller contract
    uint public num;
    address public sender;
    uint public value;

    function setVars(uint _num) public payable {
        num = _num;
        sender = msg.sender;
        value = msg.value;
    }
}
