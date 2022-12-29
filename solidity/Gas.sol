// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract Gas {
    uint public i = 0;

    // We are going to try to use all gass to cause a transaction fail.
    // State changes are undone.
    // Gas spent are not refunded.
    function forever() public {
        // This while loop will run until in spend all gas.
        while (true) {
            i += 1;
        }
    }

    function increase() public {
        i += 1;
    }
}
