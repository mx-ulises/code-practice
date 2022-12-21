// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract Variables {
    // State variables are stored in the blockchain.
    string public state_var_text = "Hello world";
    uint public state_var_uint = 69;

    function doSomething() public {
        // Local variables are not stored in the blockchain.
        uint local_var = 420;

        // Global variables with info about the blockchain
        uint timestamp = block.timestamp; // Current block timestamp
        address sender = msg.sender; // Address of the caller
    }
}
