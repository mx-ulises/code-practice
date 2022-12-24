impl Solution {
    fn solution_one(nums: Vec<i32>) -> Vec<i32> {
        let mut output = Vec::new();
        for x in &nums {
            output.push(nums[*x as usize]);
        }
        return output;
    }

    fn solution_two(mut nums: Vec<i32>) -> Vec<i32> {
        for i in 0..nums.len() {
            let num = nums[nums[i] as usize] % 1000;
            nums[i] += num * 1000;
        }
        for i in 0..nums.len() {
            nums[i] = nums[i] / 1000;
        }
        return nums;
    }

    pub fn build_array(mut nums: Vec<i32>) -> Vec<i32> {
        return Solution::solution_two(nums);
    }
}
