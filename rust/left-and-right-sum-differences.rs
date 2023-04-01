impl Solution {
    pub fn left_rigth_difference(nums: Vec<i32>) -> Vec<i32> {
        let mut left_sum: i32 = 0;
        let mut right_sum: i32 = nums.iter().sum();
        let mut differences = Vec::new();
        for x in nums {
            right_sum -= x;
            let diff = (right_sum - left_sum).abs();
            differences.push(diff);
            left_sum += x;
        }
        return differences;
    }
}
