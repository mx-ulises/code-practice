// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

interface IRemoteContract {
    function counter() external view returns (uint);
    function increment() external;
}
