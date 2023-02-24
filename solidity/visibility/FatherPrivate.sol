// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract FatherPrivate {
    function privateFunction() private pure returns(string memory) {
        return "Private Function Called";
    }

    function callPrivateFunction() public pure returns(string memory) {
        return string.concat("Handler -> ", privateFunction());
    }
}
