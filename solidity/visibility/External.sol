// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract External {
    function externalFunction() external pure returns(string memory) {
        return "External Function Called";
    }
}
