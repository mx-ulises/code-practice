// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract Constants {
    // Constants cannot change and the constant name is written in upper cases
    address public constant CONSTANT_ADDRESS = 0x777788889999AaAAbBbbCcccddDdeeeEfFFfCcCc;
    uint public constant CONSTANT_VALUE = 420;

    function getConstant() public view returns (uint) {
        //CONSTANT_VALUE = 69; <- this doesn't compile
        return CONSTANT_VALUE + 3;
    }
}
