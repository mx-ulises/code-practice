// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract Payable {
    // Payable address can recieve Ether
    address payable public owner;

    // Payable constructor that can recieve Ether
    constructor() payable {
        owner = payable(msg.sender);
    }

    // Function to deposit Ether in the contract.
    function deposit() public payable {}

    // Function that is not payable and cannot be called with Ether
    function notPayable() public {}

    // Function to move Ether from this contract to owner address
    function withdraw() public {
        // Get balance from the address of this contract
        uint amount = address(this).balance;
        // Call the owner address to send all the balance
        (bool success, ) = owner.call{value: amount}("");
        require(success, "Failed to send Ether to owner");
    }

    // Function to transfer Ether from this contract to another address.
    function transfer(address payable _to, uint _amount) public {
        (bool success, ) = _to.call{value: _amount}("");
        require(success, "Failed to send Ether to account");
    }
}
