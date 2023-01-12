// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

// Importing Enum
import "./libs/StatusEnum.sol";

contract Enum {
    // Default value is the first element listed in the definition.
    Status public status;

    function get() public view returns (Status) {
        return status;
    }

    // You can use enum as an argument type, they are used as uint
    function set(Status _status) public {
        status = _status;
    }

    // This is how you assign a new value to an enum variable
    function cancel() public {
        status = Status.Canceled;
    }

    // Delete operator resets the enum to the default value
    function reset() public {
        delete status;
    }
}