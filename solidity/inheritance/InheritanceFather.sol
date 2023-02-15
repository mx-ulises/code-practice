// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

import "./InheritanceGrandfather.sol";

contract InheritanceFather is InheritanceGrandfather {
    function who_am_i() public pure virtual override returns (string memory) {
        return "Father";
    }
}
