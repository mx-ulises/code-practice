use std::cmp;
use std::collections::BinaryHeap;


impl Solution {
    pub fn maximum_product(nums: Vec<i32>) -> i32 {
        // Store for the smallest and largest elements
        let mut max_heap = BinaryHeap::new();
        let mut min_heap = BinaryHeap::new();

        // Get the three largest and the two smallest elements
        for x in nums {
            min_heap.push(x);
            max_heap.push(-x);
            if 3 < max_heap.len() {
                max_heap.pop();
            }
            if 2 < min_heap.len() {
                min_heap.pop();
            }
        }

        // Get product of the 3 largest
        let mut option_maximals = 1;
        while 1 < max_heap.len() {
            option_maximals *= -max_heap.pop().unwrap();
        }
        option_maximals *= -max_heap.peek().unwrap();

        // Get the product of the largest and the 2 smallest
        let mut option_minimals = -max_heap.pop().unwrap();
        while 0 < min_heap.len() {
            option_minimals *= min_heap.pop().unwrap();
        }

        // Return the maximum number of these two options
        return cmp::max(option_minimals, option_maximals);
    }
}
