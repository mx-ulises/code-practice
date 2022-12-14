// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract EtherUnits {

    // How much is wei?
    uint public wei1 = 1 wei;
    uint public wei2 = 2 wei;
    uint public wei100 = 100 wei;

    // Check if a number is Wei
    function isWei(uint _num) public view returns(bool) {
        return _num == 1 wei;
    }

    // How much is Ether
    uint public ether1 = 1 ether;
    uint public ether4 = 4 ether;
    uint public wei2ether = 1e18 wei;
    uint public uint2ether = 1e18;

    // Check if a number is Ether
    function isEther(uint _num) public view returns(bool) {
        return _num == 1 ether;
    }
}
