// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract ErrorRequire {
    mapping(uint => bool) public mapper;

    function testRequire(uint _i) public {
        require(100 <= _i && _i <= 200, "Input should be in [100, 200] range");
        require(mapper[_i] == false, "Input is already populated");
        mapper[_i] = true;
    }
}
