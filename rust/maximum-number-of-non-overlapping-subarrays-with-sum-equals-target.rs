use std::collections::HashMap;

impl Solution {
    pub fn max_non_overlapping(nums: Vec<i32>, target: i32) -> i32 {
        let mut cummulative_map:HashMap<i32, i32> = HashMap::new();
        cummulative_map.insert(0, 0);
        let mut cummulative:i32 = 0;
        let mut last_end:i32 = -1;
        let mut sub_arrays_count:i32 = 0;
        for i in 0..nums.len() {
            cummulative += nums[i];
            let key = cummulative - target;
            if cummulative_map.contains_key(&key) && last_end < *(cummulative_map.get(&key).unwrap()) {
                last_end = i as i32;
                sub_arrays_count += 1;
            }
            cummulative_map.insert(cummulative, (i + 1) as i32);
        }
        return sub_arrays_count
    }
}
