// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract NestedMapping {
    // Nested mapping when a map has another map as value
    mapping(address => mapping(uint => uint)) addressMultyBalance;

    function get(address _address, uint _currency) public view returns (uint) {
        // We can return default values for nested mapping that are not initialized
        return addressMultyBalance[_address][_currency];
    }

    function set(address _address, uint _currency, uint _balance) public {
        // Similar as regular maps, we can update or set values in nested maps.
        addressMultyBalance[_address][_currency] = _balance;
    }

    function remove(address _address, uint _currency) public {
        // Similar as regular maps, we can remove keys from nested maps.
        delete addressMultyBalance[_address][_currency];
    }
}
