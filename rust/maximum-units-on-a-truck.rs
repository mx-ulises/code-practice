use std::collections::BinaryHeap;
use std::collections::HashMap;
use std::cmp;

impl Solution {
    pub fn maximum_units(box_types: Vec<Vec<i32>>, truck_size: i32) -> i32 {
        let mut pending_boxes:i32 = truck_size;
        let mut total_units:i32 = 0;
        let mut heap:BinaryHeap<i32> = BinaryHeap::new();
        let mut map:HashMap<i32,i32> = HashMap::new();
        for pair in box_types {
            let boxes = *(pair.get(0).unwrap());
            let units = *(pair.get(1).unwrap());
            if map.get(&units) == None {
                map.insert(units, 0);
                heap.push(units);
            }
            map.insert(units, map.get(&units).unwrap() + boxes);
        }
        while !heap.is_empty() && 0 < pending_boxes {
            let units = heap.pop().unwrap();
            let boxes = cmp::min(*(map.get(&units).unwrap()), pending_boxes);
            total_units += units * boxes;
            pending_boxes -= boxes;
        }
        return total_units;
    }
}
