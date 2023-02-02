// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract FunctionModifier {
    uint public total_tokens = 1000;
    uint public constant LOWER_LIMIT = 100;

    // Modifier to check we are not substracting more than lower limit.
    modifier checkLowerLimit(uint _withdrawAmmount) {
        require(LOWER_LIMIT <= total_tokens - _withdrawAmmount, "You are substracting too much");
        // Special caracter for a modifier to tell Solidity to execute the code.
        _;
    }

    // Modifier will be executed as part of the function.
    function witdraw(uint _withdrawAmmount) public checkLowerLimit(_withdrawAmmount) {
        total_tokens = total_tokens - _withdrawAmmount;
    }
}
