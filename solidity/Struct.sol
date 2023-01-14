// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract Struct {
    struct Todo {
        string activity;
        bool completed;
    }

    // Creating an array of Todo elements
    Todo[] public todo_list;

    function create(string  calldata _activity) public {
        // There are three ways to initialize an struct:
        // 1. Constructor Function-like
        Todo memory todo_1 = Todo(_activity, false);
        todo_list.push(todo_1);

        // 2. key-value pair input
        Todo memory todo_2 = Todo({activity: _activity, completed: false});
        todo_list.push(todo_2);

        // 3. Initialize and update elements one by one
        Todo memory todo_3;
        todo_3.activity = _activity;
        todo_list.push(todo_3);
    }

    function complete_activity(uint _index) public {
        Todo storage todo = todo_list[_index];
        todo.completed = true;
    }
}
