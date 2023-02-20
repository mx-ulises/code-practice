// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

import "./InheritanceCallGrandfather.sol";

contract InheritanceCallFather is InheritanceCallGrandfather {
    function foo() public virtual {
        emit Log("Father.foo() called,");
    }

    function bar() public virtual {
        emit Log("Father.bar() called.");
    }
}
