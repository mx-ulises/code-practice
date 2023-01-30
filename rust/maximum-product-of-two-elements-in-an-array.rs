impl Solution {
    pub fn max_product(nums: Vec<i32>) -> i32 {
        let mut max_1 = 0;
        let mut max_2 = 0;
        for x in nums {
            if max_1 < x {
                max_2 = max_1;
                max_1 = x;
            } else if max_2 < x {
                max_2 = x;
            }
        }
        return (max_1 - 1) * (max_2 - 1);
    }
}
