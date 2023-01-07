// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract Array {
    // Non-Fixed size arrays
    uint[] public arrayEmpty;
    uint[] public arrayFilled = [1, 2, 3];

    // Fixed array size, elements are initialized with default value
    uint[10] public arrayFixed;

    function get(uint i) public view returns(uint) {
        // return element in array in position i
        return arrayFilled[i];
    }

    function push(uint x) public {
        // Add element at the end of the array, increase lenght by 1
        arrayFilled.push(x);
    }

    function pop() public {
        // Remove the last element from the array, decrease lenght by 1
        arrayFilled.pop();
    }

    function getLength() public view returns (uint) {
        // Return the count of elements of the array.
        return arrayFilled.length;
    }

    function remove(uint i) public {
        // Reset the value at index i to the default value. It doesn't decrease lenght
        delete arrayFilled[i];
    }

    function inMemoryArray(uint n) public {
        // Create array in memory. It only allows fixed size arrays
        uint[] memory a = new uint[](n);
    }
}
