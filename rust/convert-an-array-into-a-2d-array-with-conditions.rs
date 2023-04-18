impl Solution {
    pub fn find_matrix(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        nums.sort();
        let mut output = Vec::new();
        let mut j = 0;
        for i in 0..nums.len() {
            if i == 0 || nums[i - 1] != nums[i] {
                j = 0;
            }
            if j == output.len() {
                output.push(Vec::new());
            }
            output[j].push(nums[i]);
            j += 1;
        }
        return output;
    }
}
