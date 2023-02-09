// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract ConstructorOne {
    string public name;

    constructor(string memory _name) {
        name = _name;
    }
}
