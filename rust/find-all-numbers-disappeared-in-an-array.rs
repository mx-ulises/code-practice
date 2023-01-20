se std::collections::HashSet;

impl Solution {
    pub fn find_disappeared_numbers(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len() as i32 + 1;
        let nums_set: HashSet<i32> = nums.into_iter().collect();
        let mut output = Vec::new();
        for i in 1..n {
            if !nums_set.contains(&i) {
                output.push(i);
            }
        }
        return output;
    }
}
