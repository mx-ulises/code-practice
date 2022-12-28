// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract EtherUnits {
    // 1 wei is equal to 1
    uint public oneWei = 1 wei;
    bool public isOneWei = 1 wei == 1;

    // 1 Ether is equial to 10^18 wei
    uint public oneEther = 1 ether;
    bool public isOneEther = 1 ether == 1e18;
}
