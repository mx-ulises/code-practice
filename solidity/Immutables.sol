// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract Immutables {

    // Immutable variables are like constants and can be only set inside the constructor but not afterwards.
    address public immutable ADDRESS;
    uint public immutable VALUE;

    constructor(uint _input) {
        ADDRESS = msg.sender;
        VALUE = _input;
    }

    function getImmutable() public view returns (uint) {
        //VALUE = 69; <- this doesn't compile
        return VALUE + 3;
    }
}
