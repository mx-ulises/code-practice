// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

import "./RemoteContract.sol";

contract TryCatch {
    event Log(string message);
    event LogBytes(bytes data);

    RemoteContract public remoteContract;

    constructor() {
        remoteContract = new RemoteContract(msg.sender);
    }

    function tryCatchExternalCall(uint _x) public {
        try remoteContract.myFunc(_x) returns (string memory result) {
            emit Log(result);
        } catch {
            emit Log("External call failed");
        }
    }
}
