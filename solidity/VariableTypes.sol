// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract VariableTypes {
    // State variables that are stored on the blockchain
    string public text = "Hello world";
    uint public num = 1988;

    function doSomething() public {
        // Local variables that won't exist in the blockchain
        uint i = 1234;
    }

    function getSender() public view returns (address) {
        return msg.sender; // Address of the caller
    }

    function getTimestamp() public view returns (uint) {
        return block.timestamp; // Current Block timestamp
    }
}
