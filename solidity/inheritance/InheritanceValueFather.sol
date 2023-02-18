// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract InheritanceValueFather {
    string public who_i_am = "Father";

    function get_who_i_am() public view returns (string memory) {
        return who_i_am;
    }
}
