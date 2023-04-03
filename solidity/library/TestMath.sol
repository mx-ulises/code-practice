// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

import "./Math.sol";

contract TestMath {
    function testPow(uint base, uint p) public pure returns (uint) {
        return Math.pow(base, p);
    }
}
