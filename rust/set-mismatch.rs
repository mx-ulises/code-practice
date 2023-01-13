impl Solution {
    pub fn find_error_nums(nums: Vec<i32>) -> Vec<i32> {
        let mut s = vec![0; nums.len()];
        for x in nums {
            s[x as usize - 1] += 1;
        }
        let mut repeated = 0;
        let mut missing = 0;
        for i in 0..s.len() {
            if s[i] == 0 {
                missing = i as i32 + 1;
            } else if s[i] == 2 {
                repeated = i as i32 + 1;
            }
        }
        return vec![repeated, missing];
    }
}
