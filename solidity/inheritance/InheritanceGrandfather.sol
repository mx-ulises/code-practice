// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract InheritanceGrandfather {
    function who_am_i() public pure virtual returns (string memory) {
        return "Grandfather";
    }
}
