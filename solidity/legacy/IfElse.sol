// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract IfElse {

    function checkSign(int _num) public pure returns(int) {
        if (_num < 0) {
            return -1;
        } else if (0 < _num) {
            return 1;
        } else {
            return 0;
        }
    }

    function isPositive(int _num) public pure returns(bool) {
        return 0 < _num? true : false;
    }

}
