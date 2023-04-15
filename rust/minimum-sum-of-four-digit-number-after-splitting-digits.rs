use std::collections::BinaryHeap;

impl Solution {
    pub fn minimum_sum(mut num: i32) -> i32 {
        let mut heap = BinaryHeap::new();
        let mut result = 0;
        while 0 < num {
            let d = num % 10;
            heap.push(-d);
            num /= 10;
        }
        while !heap.is_empty() {
            result *= 10;
            result -= heap.pop().unwrap() + heap.pop().unwrap();
        }
        return result;
    }
}
