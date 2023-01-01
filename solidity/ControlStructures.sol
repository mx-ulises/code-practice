// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract ControlStructures {

    function if_else(uint _x) public pure returns (uint) {
        if (_x < 10) {
            return 1;
        } else if (_x < 20) {
            return 2;
        } else {
            return 3;
        }
    }

    function ternary(uint _x) public pure returns (bool) {
        // Instead of writing if-else, we can call the ternary operator.
        // Equivalent code is:
        // if (_x < 20) {
        //     return true;
        // } else {
        ///    return false;
        // }
        return _x < 20 ? true : false;
    }
}
