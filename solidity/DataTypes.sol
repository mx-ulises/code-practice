// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract DataTypes {
    // Boolean [true or false]
    bool public boolean_var = true;
    bool public boolean_default; // Default value: false

    /*
    uint is unsiged integer, meaning the value will be equals or greater than 0.
    It has different sizes:
        uint8   ranges from 0 to 2^8 - 1
        uint16  ranges from 0 to 2^16 -1
        ...
        uint256 ranges from 0 to 2^256 -1
    */

    uint8 public uint8Var = 255;
    uint public uintVar = 35000; // uint is same as uint256
    uint public uintDefault; // Default value is 0
    uint public minUint = type(uint).min;
    uint public maxUint = type(uint).max;

    /*
    int is integer that can take both negative and positive values.
    It has different sizes
        int8    ranges from -(2^7) to 2^7 - 1
        int16   ranges from -(2^15) to 2^15 -1
        ...
        int256  ranges from -(2^255) to 2^255 -1
    */

    int16 public int16Var = 456;
    int public intVar = -33; // int is same as int256
    int public intDefault; // Default value is 0
    int public minInt = type(int).min;
    int public maxInt = type(int).max;

    /*
    Byte represent a sequence of bytes. There are two type of bytes types :
        fixed-sized byte arrays
        dynamically-sized byte arrays.
     
    The term bytes represents a dynamic array of bytes.  It’s a shorthand
    for byte[].
    */

    bytes1 public bytes1Var = 0xb5; // [10110101]
    bytes1 public bytes1Default; // Default value is 0x00

    // Adresses to Wallets
    address public addressVar = 0xCA35b7d915458EF540aDe6068dFe2F44E8fa733c;
    address public addressDefault; // Default value is 0x0000000000000000000000000000000000000000
}
