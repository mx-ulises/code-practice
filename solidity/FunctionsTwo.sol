// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract FunctionsTwo {
    uint[] array;

    // We can recieve arrays as input of functions
    function arrayInput(uint[] memory _array) public {
        uint total;
        for(uint i = 0; i < _array.length; i++) {
            total += _array[i];
        }
        array.push(total);
    }

    // We can have arrays as output of functions
    function arrayOutput() public view returns(uint[] memory) {
        return array;
    }
}
