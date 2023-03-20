// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

import "./Car.sol";

contract CarFactory {
    Car[] public cars;

    function create(address _owner, string memory _model) public {
        Car car = new Car(_owner, _model);
        cars.push(car);
    }

    function getCar(uint _index)
        public
        view
        returns (address owener, string memory model, address carAddr, uint balance)
    {
        Car car = cars[_index];
        return(car.owner(), car.model(), car.carAddr(), address(car).balance);
    }
}
