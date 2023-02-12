// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

import "./libs/ConstructorOne.sol";

contract ConstructorTwo is ConstructorOne("Nombre") {
    string public lastname;

    constructor(string memory _lastname) {
        lastname = _lastname;
    }
}
