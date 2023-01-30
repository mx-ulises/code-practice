// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract ErrorAssert {

    uint public num;

    function addUp() public {
        // Test Assert will fail after executing this
        num += 1;
    }

    function testAssert() public view {
        assert(num == 0);
    }
}
