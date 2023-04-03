// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

library Math {
    function pow(uint base, uint p) internal pure returns (uint output) {
        output = 1;
        while (0 < p) {
            output *= base;
            p--;
        }
    }
}
