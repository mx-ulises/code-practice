// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

// import Foo.sol from github
import "https://github.com/mx-ulises/code-practice/blob/main/solidity/import/Foo.sol";

contract ImportGithub {
    Foo public foo = new Foo();

    function getFooName() public view returns (string memory) {
        return foo.name();
    }
}
