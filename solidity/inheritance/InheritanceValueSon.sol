// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

import "./InheritanceValueFather.sol";

contract InheritanceValueSon is InheritanceValueFather {
    constructor() {
        who_i_am = "Son";
    }
}
