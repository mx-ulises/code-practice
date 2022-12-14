// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract Array {

    // Ways to declare arrays?
    // Dynamic array that can add and remove elements
    uint[] public dynamicEmptyArray;
    // Same as above, it is prefilled.
    uint[] public dynamicPrefilledArray = [10, 20, 30];
    // Fixed Array, cannot change the size, in this case it is is initialized
    // with default values.
    uint[10] public fixedArray;

    // Soliditu can return the full array, but it is bad practice as it can
    // return an extremely large array.
    function getArr() public view returns (uint[] memory) {
        return dynamicEmptyArray;
    }

    // Append a number to the array
    function push(uint x) public {
        dynamicEmptyArray.push(x);
        dynamicPrefilledArray.push(x);
        //fixedArray.push(x); not allowed
    }

    // Remove last element from array
    function pop() public {
        dynamicEmptyArray.pop();
        dynamicPrefilledArray.pop();
        //fixedArray.pop(); not allowed
    }

    // Return lenght of Dynamic Empty Array
    function getLenghtDynamicEmpty() public view returns (uint) {
        return dynamicEmptyArray.length;
    }

    // Return lenght of Dynamic Prefilled Array
    function getLenghtDynamicPrefilled() public view returns (uint) {
        return dynamicPrefilledArray.length;
    }

    // Return lenght of Fixed Array
    function getLenghtFixed() public view returns (uint) {
        return fixedArray.length;
    }

    // Delete doesn't change value, just return to default value.
    function remove(uint index) public {
        delete dynamicEmptyArray[index];
        delete dynamicPrefilledArray[index];
        delete fixedArray[index];
    }

    function inMemoryArray() external {
        // Create in-memory arrays, only fixed size are allowed.
        uint[] memory memoryArray = new uint[](5);
        uint[5] memory memoryArray2;
        //uint[] memory memoryArray3; not needed
        for(uint i = 0; i < 5; i++) {
            memoryArray[i] = i * 10;
            memoryArray2[i] = i * 10;
            //memoryArray3.push(i * 10); not allowed
        }
    }

}
