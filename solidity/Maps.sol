// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract Maps {
    // Mappings require a Key Type and a Value Type.
    // Key type can be uint, address or bytes
    // Value type can be any type

    // Simple Mapping from address to uint
    mapping(address => uint) simpleMap;
    // Nested Mapping, from an address to another mapping from uint to uint.
    mapping(address => mapping(uint => uint)) nestedMap;

    function getSimple(address _key) public view returns (uint) {
        // Mappings always return values, if it is not set, then it will return
        // the default value type
        return simpleMap[_key];
    }

    function getNested(address _key1, uint _key2) public view returns (uint) {
        // Return nested value
        return nestedMap[_key1][_key2];
    }

    function setSimple(address _key, uint _value) public {
        // Set the element with the provided key with a value
        simpleMap[_key] = _value;
    }

    function setNested(address _key1, uint _key2, uint _value) public {
        // Set nested value
        nestedMap[_key1][_key2] = _value;
    }

    function removeSimple(address _key) public {
        // Remove the element with the provide key from the map
        delete simpleMap[_key];
    }

    function removeAddressNested(address _key1, uint _key2) public {
        // We can only remove nested values from nested maps
        delete nestedMap[_key1][_key2];
    }

}
