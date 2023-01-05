// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract Mapping {
    // A map requires define the key type and value type
    mapping (address => uint) public addressBalance;

    function get(address _address) public view returns (uint) {
        // To access the value we need the key only.
        // If the value was never set, it will return the default value of the value type.
        return addressBalance[_address];
    }

    function set(address _address, uint _balance) public {
        // Set or update value for the key in the map
        addressBalance[_address] = _balance;
    }

    function remove(address _address) public {
        // We use the delete operator on the map using the key to reset the value
        delete addressBalance[_address];
    }
}
