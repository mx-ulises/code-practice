// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract Structs {
    // Struct that specify the schema of the objects
    struct User {
        address id;
        string name;
        uint balance;
    }

    User[] public users;

    function createUser1(string memory _name) public {
        // Fill struct on object creation time passing ordered params
        User memory user = User(msg.sender, _name, 0);
        users.push(user);
    }

    function createUser2(string memory _name) public {
        // Fill struct on object creation time passing value definiton
        User memory user = User({
           id: msg.sender,
           name: _name,
           balance: 0}
        );
        users.push(user);
    }

    function createUser3(string memory _name) public {
        // Declare struct object with defaul value
        User memory user;
        user.id = msg.sender;
        user.name = _name;
        users.push(user);
    }

    function get(uint _index) public view returns (address id, string memory name, uint balance) {
        User storage user = users[_index];
        // This is the way we return multiple values
        return (user.id, user.name, user.balance);
    }

    function addBalance(uint _index, uint ammount) public {
        User storage user = users[_index];
        user.balance += ammount;
    }
}
