// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract Fallback {
    event Log(string func, uint gas);

    // Fallback function must be declared as external
    fallback() external payable {
        // Send / Transfer (forwards 2300 gas to this fallback function)
        // call (forwards all the gas)
        emit Log("fallback", gasleft());
    }

    // Recieve is a varaint of fallback that is triggered when msg.data is empty
    receive() external payable {
        emit Log("receive", gasleft());
    }

    function getBalance() public view returns (uint) {
        return address(this).balance;
    }
}
