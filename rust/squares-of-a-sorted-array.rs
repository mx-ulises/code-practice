impl Solution {
    pub fn sorted_squares(nums: Vec<i32>) -> Vec<i32> {
        let mut left = 0;
        let mut left_square = nums[left] * nums[left];
        let mut right = nums.len() - 1;
        let mut right_square = nums[right] * nums[right];
        let mut output = vec![];
        while left < right {
            if left_square < right_square {
                output.push(right_square);
                right -= 1;
                right_square = nums[right] * nums[right]
            } else {
                output.push(left_square);
                left += 1;
                left_square = nums[left] * nums[left];
            }
        }
        output.push(left_square);
        output.reverse();
        return output;
    }
}
