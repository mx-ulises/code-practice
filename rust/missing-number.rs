impl Solution {
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        let vec_sum:i32 = nums.iter().sum();
        let total_sum:i32 = (nums.len() * (nums.len() + 1)) as i32 / 2;
        return total_sum - vec_sum;
    }
}
