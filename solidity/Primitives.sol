// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract Primitives {
    bool public binary = true;

    /*
    uint stands for unsigned integer, meaning that non-negative integers
    are allowed. Size availables are:
        uint8   -> ranges from 0 to (2 ** 8 - 1)
        uint16  -> ranges from 0 to (2 ** 16 - 1)
        ...
        uint256 -> ranges from 0 to (2 ** 256 - 1)
    */

    uint8 public u8 = 1;
    uint256 public u256 = 455;
    uint public u = 123; // uint is alias of uint256

    /*
    Negative numberes are allowed for int types. Like uint, different ranges
    are available from int8 to int256:
        int128  -> ranges from (-2 ** 127) to (2 ** 127 - 1)
        int256  -> ranges from (-2 ** 255) to (2 ** 255 - 1)
    */

    int8 public i8 = -1;
    int256 public i256 = 123;
    int public i = -2345; // int is alias of int256

    // We can get minimuns and maximums of int
    int public minInt = type(int).min;
    int public maxInt = type(int).max;

    // There is a datatype for address in Etherium blockchain
    address public a = 0xCA35b7d915458EF540aDe6068dFe2F44E8fa733c;

    /*
    In Solidity, the data type byte represent a sequence of bytes.
    Solidity presents two type of byte types:
        - Fixed-sized byte arrays
        - Dinamically-sized byte arrays

    The rerm bytes in Solidity represents a dynamic array of bytes.
    It's a shorthand for byte[].
    */

    bytes1 public b1 = 0xb5; //  [10110101]
    bytes1 public b2 = 0x56; //  [01010110]

    // Default values are assigned to variables with unnasigned values.
    bool public defaultBinary; // false
    uint public defaultUint; // 0
    int public defaultInt; // 0
    address public defaultAddress; // 0x0000000000000000000000000000000000000000
}
