impl Solution {
    pub fn is_ugly(mut n: i32) -> bool {
        if n == 0 {
            return false;
        }
        let PRIME_FACTORS: Vec<i32> = vec![2, 3, 5];
        for factor in PRIME_FACTORS {
            while n % factor == 0 {
                n = n / factor;
            }
        }
        return n == 1;
    }
}
