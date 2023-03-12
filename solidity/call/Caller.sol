// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract Caller {
    event Response(bool success, bytes data);

    // We know the address and the function in the contract
    function testCallFoo(address payable _addr) public payable {
        (bool success, bytes memory data) = _addr.call{value: msg.value, gas: 5000}(
            abi.encodeWithSignature("foo(string,uint256)", "call foo", 123)
        );
        emit Response(success, data);
    }

    // Calling a function that doesn't exist and call fallback
    function testCallDoesNotExist(address payable _addr) public payable {
        (bool success, bytes memory data) = _addr.call{value: msg.value}(
            abi.encodeWithSignature("doesNotExist()")
        );
        emit Response(success, data);
    }
}
