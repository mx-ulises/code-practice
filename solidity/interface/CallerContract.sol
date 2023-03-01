// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

import "./IRemoteContract.sol";

contract CallerContract {
    function call_count(address _remote_contract_address) external view returns (uint) {
        return IRemoteContract(_remote_contract_address).counter();
    }

    function call_increment(address _remote_contract_address) external {
        IRemoteContract(_remote_contract_address).increment();
    }
}
