// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract ReceiveEther {
    // Function to receive Ether with msg.data Empty
    receive() external payable {}

    // Function to recieve Ether when there is message or there is no Receive().
    fallback() external payable {}

    function getBalance() public view returns (uint) {
        return address(this).balance;
    }
}
