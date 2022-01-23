// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract InfiniteGas {
    // State variable.
    uint public i = 0;

    // This variable uses tons of gas, it should fail eventually.
    function longRun() public {
        // Spend 1 Ether on operations.
        uint j = 0;
        while (j < 1 ether) {
            j += 1;
            i += 1;
        }
    }

    function infinite() public {
        // This function use infinite gas and will fail eventually without
        // refounding your gas but not changing state vars.
        while (true) {
            i += 1;
        }

    }
}
