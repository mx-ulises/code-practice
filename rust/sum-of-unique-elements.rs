use std::collections::HashMap;

impl Solution {
    pub fn sum_of_unique(nums: Vec<i32>) -> i32 {
        let mut nums_count = HashMap::new();
        for x in nums {
            if !nums_count.contains_key(&x) {
                nums_count.insert(x, 0);
            }
            nums_count.insert(x, nums_count.get(&x).unwrap() + 1);
        }
        let mut output = 0;
        for (k, v) in nums_count {
            if v == 1 {
                output += k;
            }
        }
        return output;
    }
}
