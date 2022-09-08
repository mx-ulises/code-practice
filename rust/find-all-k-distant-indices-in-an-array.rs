use std::cmp;

impl Solution {
    pub fn find_k_distant_indices(nums: Vec<i32>, key: i32, k: i32) -> Vec<i32> {
        let mut output:Vec<i32> = Vec::new();
        let mut min:i32 = 0;
        let max:i32 = nums.len() as i32;
        for i in 0..max {
            if nums[i as usize] == key {
                let start:i32 = cmp::max(min, i - k);
                let end:i32 = cmp::min(max, i + k + 1);
                for j in start..end {
                    output.push(j);
                }
                min = end;
            }
        }
        output
    }
}
