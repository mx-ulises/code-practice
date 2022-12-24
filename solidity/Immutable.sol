// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract Immutable {
    // Convention is to use uppercase as in contants
    address public immutable OWNER_ADDRESS;
    uint public immutable FAVORITE_NUMBER;

    // Immutable variables can be set only in the constructor
    constructor(uint _favoriteNumber) {
        OWNER_ADDRESS = msg.sender;
        FAVORITE_NUMBER = _favoriteNumber;
    }

}
