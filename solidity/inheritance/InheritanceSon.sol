// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

import "./InheritanceFather.sol";
import "./InheritanceMother.sol";

contract InheritanceSon is InheritanceFather, InheritanceMother {
    function who_am_i() public pure virtual override(InheritanceFather, InheritanceMother) returns (string memory) {
        return super.who_am_i();
    }
}
