impl Solution {
    pub fn pivot_index(nums: Vec<i32>) -> i32 {
        let mut total_sum: i32 = nums.iter().sum();
        let mut current_sum: i32 = 0;
        for i in 0..nums.len() {
            total_sum -= nums[i];
            if current_sum == (total_sum) {
                return i as i32;
            }
            current_sum += nums[i];
        }
        return -1;
    }
}
