// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract BaseVisibility {
    // State variables
    string private privateVar = "my private variable";
    string internal internalVar = "my internal variable";
    string public publicVar = "my public variable";

    function getPrivate() public view returns (string memory) {
        return privateVar;
    }

    function getInternal() public view returns (string memory) {
        return internalVar;
    }
}
