// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract Loops {
    function forExample(uint k) public pure returns (uint) {
        uint output = 0;
        for (uint i = 0; i <= k; i++) {
            if (i == 3) {
                // Skip execution of this iteration and continue with the next.
                continue;
            }
            if (i == 5) {
                // Break the loop and continue execution after it.
                break;
            }
            output = i;
        }
        return output;
    }

    function whileExample(uint k) public pure returns (uint) {
        uint output = 0;
        // Not recommended as we can have outbouded requests that can burn gas
        while (output <= k) {
            output += 1;
        }
        return output;
    }
}
