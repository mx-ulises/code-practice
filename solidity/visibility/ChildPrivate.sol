// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

import "./FatherPrivate.sol";

contract ChildPrivate is FatherPrivate {
    function callFatherPrivateFunction() public pure returns (string memory) {
        // Not possible to call private functions from base
        //return privateFunction();
        return "Not possible";
    }
}
