// SPDX-Licence-Identifier: MIT
pragma solidity ^0.8.13;

contract SendEther {
    function sendViaTransfer(address payable _to) public payable {
        // This function is no longer recommended.
        _to.transfer(msg.value);
    }

    function sendViaSend(address payable _to) public payable {
        // This function is no longer recommended.
        // Send returns boolean indicating success or failure
        bool sent = _to.send(msg.value);
        require(sent, "Failed to send Ether via 'send'");
    }

    function sendViaCall(address payable _to) public payable {
        // This is the current recommended way to use.
        // Call returns boolean indicating success or failure
        (bool sent, bytes memory data) = _to.call{value: msg.value}("");
        require(sent, "Failed to send Ether via 'call'");
    }
}
