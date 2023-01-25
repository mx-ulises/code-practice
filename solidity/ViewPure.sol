// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract ViewPure {
    uint public x = 100;

    // Promise not to modify the state (read only)
    function addToX(uint y) public view returns (uint) {
        return x + y;
    }

    // Promise not to modify or read from the state (Static function, just placed in the contract)
    function add(uint i, uint j) public pure returns (uint) {
        return i + j;
    }
}
