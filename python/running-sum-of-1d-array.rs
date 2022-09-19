impl Solution {
    pub fn running_sum(nums: Vec<i32>) -> Vec<i32> {
        let mut output:Vec<i32> = Vec::new();
        let mut sum:i32 = 0;
        for x in nums {
            sum += x;
            output.push(sum);
        }
        return output;
    }
}
