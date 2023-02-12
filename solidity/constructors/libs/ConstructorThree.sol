// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract ConstructorThree {
    string public lastname;

    constructor(string memory _lastname) {
        lastname = _lastname;
    }
}
