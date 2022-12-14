// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract Counter {

    // unsigned counter value
    uint _count;

    // Function to get the current counter value
    function get() public view returns (uint) {
        return _count;
    }

    // Function to increment counter by 1
    function inc() public {
        _count += 1;
    }

    // Function to decrement counter by 1
    function dec() public {
        _count -= 1;
    }
}
