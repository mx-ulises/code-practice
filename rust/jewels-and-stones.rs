use std::collections::HashSet;

impl Solution {
    pub fn num_jewels_in_stones(jewels: String, stones: String) -> i32 {
        let mut jewels_set = HashSet::new();
        let mut count = 0;
        for jewel in jewels.chars() {
            jewels_set.insert(jewel);
        }
        for stone in stones.chars() {
            if jewels_set.contains(&stone) {
                count += 1;
            }
        }
        return count;
    }
}
