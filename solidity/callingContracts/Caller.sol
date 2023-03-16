// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

import "./Callee.sol";

contract Caller {
    function setX(Callee _callee, uint _x) public returns (uint) {
        uint x = _callee.setX(_x);
        return x;
    }

    function setXfromAddress(address _addr, uint _x) public returns (uint) {
        Callee callee = Callee(_addr);
        return callee.setX(_x);
    }

    function setXandSendEther(Callee _callee, uint _x) public payable returns (uint, uint) {
        (uint x, uint value) = _callee.setXandSendEther{value: msg.value}(_x);
        return (x, value);
    }
}
