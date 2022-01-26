// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract Loops {
    // Utility state var to keep the track
    uint public counter = 0;

    function addTen() public {
        // Prefer the usage of For loops as they are bounded in the ammount
        // of gas to be used.
        for (uint i = 0; i < 10; i++) {
            counter += 1;
        }
    }

    function addNine() public {
        for (uint i = 0; i < 10; i++) {
            // This will skip the execution of the iteration when i = 5
            if (i == 5) continue;
            counter += 1;
        }
    }

    function addLimit() public {
        for (uint i = 0; i < 10; i++) {
            // this will break when 150 <= counter
            if (150 <= counter) break;
            counter += 1;
        }
    }

    function upTo100() public {
        // As a good practice, avoid while/do while unless you have them
        // clearly bounded. Otherwise you will have a program that spend a lot
        // of gas.
        while (counter < 100) {
            counter += 1;
        }
    }

}
