use std::cmp;

impl Solution {
    pub fn max_count(m: i32, n: i32, ops: Vec<Vec<i32>>) -> i32 {
        let mut a_min: i32 = m;
        let mut b_min: i32 = n;
        for op in ops {
            a_min = cmp::min(a_min, op[0]);
            b_min = cmp::min(b_min, op[1]);
        }
        return a_min * b_min;
    }
}
