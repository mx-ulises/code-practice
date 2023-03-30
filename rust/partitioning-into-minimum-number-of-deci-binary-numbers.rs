use std::cmp;

impl Solution {
    pub fn min_partitions(n: String) -> i32 {
        let mut min_partitions = 0;
        for d in n.chars() {
            let candidate = (d as i32) - 48;
            min_partitions = cmp::max(min_partitions, candidate);
            if min_partitions == 9 {
                break;
            }
        }
        return min_partitions;
    }
}
