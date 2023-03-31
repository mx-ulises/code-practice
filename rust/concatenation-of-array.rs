impl Solution {
    pub fn get_concatenation(nums: Vec<i32>) -> Vec<i32> {
        let cat_count = 2;
        let mut output_nums = vec![0; nums.len() * cat_count];
        for i in 0..nums.len(){
            for j in 0..cat_count {
                output_nums[i + j * nums.len()] = nums[i];
            }
        }
        return output_nums;
    }
}
