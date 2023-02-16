use std::collections::BinaryHeap;

impl Solution {
    pub fn maximum_population(logs: Vec<Vec<i32>>) -> i32 {
        let mut current_population = 0;
        let mut maximum_population = 0;
        let mut maximum_population_year = -1;
        let mut heap = BinaryHeap::new();
        for log in logs {
            heap.push((-log[0], 1));
            heap.push((-log[1], -1));
        }
        while 0 < heap.len() {
            let year = heap.peek().unwrap().0;
            current_population += heap.pop().unwrap().1;
            while 0 < heap.len() && year == heap.peek().unwrap().0 {
                current_population += heap.pop().unwrap().1;
            }
            if maximum_population < current_population {
                current_population = maximum_population;
                maximum_population_year = year;
            }
        }
        return -maximum_population_year;
    }
}
