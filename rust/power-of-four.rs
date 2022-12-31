impl Solution {
    pub fn is_power_of_four(n: i32) -> bool {
        if n < 1 {
            return false;
        }
        let x = (n as f64).log(4 as f64) as i32;
        return n == 1 || 4_f64.powi(x) as i32 == n;
    }
}
