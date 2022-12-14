// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract Enum {
    // Enum is a set of values that a variable can take
    enum Color {
        Red,
        Blue,
        Green,
        Cyan,
        Yellow,
        Purble
    }

    // The default value of an enum is the first element.
    Color public color;

    function get() public view returns(Color) {
        return color;
    }

    function set(Color _color) public {
        color = _color;
    }

    // We can access an specific value of the Enum
    function setBlue() public {
        color = Color.Blue;
    }

    // This will assign the default value to the enum.
    function reset() public {
        delete color;
    }

}
