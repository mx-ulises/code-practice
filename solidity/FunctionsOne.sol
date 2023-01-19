// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract FunctionsOne {
    // Function returning multiple values
    function multipleValues() public pure returns (uint, bool, address) {
        return (1, true, 0x5B38Da6a701c568545dCfcB03FcB875f56beddC4);
    }

    // Function returning multiple named values
    function multipleNamedValues() public pure returns (uint num, bool flag, address wallet) {
        return (2, false, 0x4B20993Bc481177ec7E8f571ceCaE8A9e22C02db);
    }

    // Function returning multiple named values by setting these output without return.
    function multipleNamedValuesWithoutReturn() public pure returns (uint num, bool flag, address wallet) {
        num = 3;
        flag = true;
        wallet = 0x14723A09ACff6D2A60DcdF7aA4AFf308FDDC160C;
    }
}
