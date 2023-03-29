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

    function tryCatchNewContract(address _owner, uint _x) public {
        try new RemoteContract(_owner) returns (RemoteContract remoteContract) {
            // you can use variable foo here
            remoteContract.myFunc(_x);
            emit Log("RemoteContract created");
        } catch Error(string memory reason) {
            // catch failing revert() and require()
            emit Log(reason);
        } catch (bytes memory reason) {
            // catch failing assert()
            emit LogBytes(reason);
        }
    }

}
