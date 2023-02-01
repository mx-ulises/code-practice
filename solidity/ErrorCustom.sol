// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract ErrorCustom {
    error InssuficientBalance(uint balance, uint withdrawAmmount);

    function testCustomError(uint _withdrawAmmount) public view {
        uint _balance = address(this).balance;
        if (_balance < _withdrawAmmount) {
            revert InssuficientBalance(_balance, _withdrawAmmount);
        }
    }
}
