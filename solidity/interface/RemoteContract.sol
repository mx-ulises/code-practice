// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract RemoteContract {
    uint public counter = 0;

    function increment() external {
        counter += 1;
    }
}
