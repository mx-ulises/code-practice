impl Solution {
    pub fn min_operations(n: i32) -> i32 {
        let avg = 1 + (n - 1);
        let m = n / 2;
        let result = m * (avg - m);
        return result;
    }
}
