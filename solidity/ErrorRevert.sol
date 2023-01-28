// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract ErrorRevert {
    mapping(uint => bool) public mapper;

    function testRevert(uint _i) public {
        if (_i < 100 || 200 < _i) {
            revert("Input should be in [100, 200] range");
        }
        if (mapper[_i] == true) {
            revert("Input is already populated");
        }
        mapper[_i] = true;
    }
}
