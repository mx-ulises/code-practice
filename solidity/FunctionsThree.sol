// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract FunctionsThree {
    function linealFormula(uint a, uint b, uint x) private pure returns (uint) {
        return a * x + b;
    }

    function regularCallFunction(uint a, uint b, uint x) external pure returns (uint) {
        return linealFormula(a, b, x);
    }

    function KeyValueCallFunction(uint a, uint b, uint x) external pure returns (uint) {
        return linealFormula({x: x, a: a, b: b});
    }
}
