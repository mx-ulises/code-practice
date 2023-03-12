// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract Caller {
    uint public num;
    uint public sender;
    uint public value;

    function setVars(address _contract, uint _num) public payable {
        (bool success, bytes memory data) = _contract.delegatecall(
            abi.encodeWithSignature("setVars(uint256)", _num)
        );
    }
}
