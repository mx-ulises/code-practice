// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

import "./libs/TodoEnum.sol";

contract TodoList {
    // Creating an array of Todo elements
    Todo[] public todo_list;

    function create(string  calldata _activity) public {
        Todo memory todo = Todo(_activity, false);
        todo_list.push(todo);
    }

    function complete_activity(uint _index) public {
        Todo storage todo = todo_list[_index];
        todo.completed = true;
    }
}
