// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract FatherInternal {
    function internalFunction() internal pure returns(string memory) {
        return "Internal Function Called";
    }

    function callInternalFunction() public pure returns(string memory) {
        return string.concat("Call from Parent -> ", internalFunction());
    }
}
