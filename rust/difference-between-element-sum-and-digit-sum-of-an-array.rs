impl Solution {
    pub fn difference_of_sum(nums: Vec<i32>) -> i32 {
        let mut diff = 0;
        for i in 0..nums.len() {
            let mut num = nums[i];
            diff += num;
            while 0 < num {
                diff -= num % 10;
                num /= 10;
            }
        }
        return diff;
    }
}
