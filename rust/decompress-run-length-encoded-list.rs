impl Solution {
    pub fn decompress_rl_elist(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len() / 2;
        let mut output = Vec::new();
        for i in 0..n {
            let freq = nums[i * 2] as usize;
            let val = nums[i * 2 + 1];
            output.append(&mut vec![val; freq]);
        }
        return output;
    }
}
