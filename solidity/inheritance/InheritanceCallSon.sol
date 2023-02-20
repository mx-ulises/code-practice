// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

import "./InheritanceCallFather.sol";
import "./InheritanceCallMother.sol";

contract InheritanceCallSon is InheritanceCallFather, InheritanceCallMother {
    function fooFather() public {
        InheritanceCallFather.foo();
    }

    function fooMother() public {
        InheritanceCallMother.foo();
    }

    function foo() public override(InheritanceCallFather, InheritanceCallMother) {
        super.foo();
        emit Log("Son.foo() called.");
    }

    function bar() public override(InheritanceCallMother, InheritanceCallFather) {
        super.bar();
        emit Log("Son.bar() called.");
    }
}
