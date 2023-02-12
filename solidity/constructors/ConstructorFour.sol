// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

import "./libs/ConstructorOne.sol";
import "./libs/ConstructorThree.sol";

contract ConstructorFour is ConstructorOne, ConstructorThree {
    string public phone;

    constructor(string memory _name, string memory _lastname, string memory _phone) ConstructorOne(_name) ConstructorThree(_lastname) {
        phone = _phone;
    }
}
