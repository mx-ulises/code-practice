// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

import "./InheritanceCallGrandfather.sol";

contract InheritanceCallMother is InheritanceCallGrandfather {
    function foo() public virtual {
        emit Log("Mother.foo() called,");
    }

    function bar() public virtual {
        emit Log("Mother.bar() called.");
    }
}
