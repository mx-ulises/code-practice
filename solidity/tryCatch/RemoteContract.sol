// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract RemoteContract {
    address public owner;

    constructor(address _owner) {
        require(_owner != address(0), "Invalid address");
        assert(_owner != 0x0000000000000000000000000000000000000001);
        owner = _owner;
    }

    function myFunc(uint x) public pure returns (string memory) {
        require(x != 0, "X should be positive");
        return "myFunc completed succesfully";
    }
}
