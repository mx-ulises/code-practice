// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

import "./FatherInternal.sol";

contract ChildInternal is FatherInternal {
    function callFatherInternalFunction() public pure returns (string memory) {
        return string.concat("Call from child ->", internalFunction());
    }
}
