impl Solution {
    fn pow(mut base: i32, mut exp: i32, MOD: i32) -> i32 {
        let mut result = 1;
        while 0 < exp {
            if exp & 1 == 1 {
                result = (result * base) % MOD;
            }
            base = (base * base) % MOD;
            exp >>= 1;
        }
        return result;
    }

    fn super_pow_handler(base: i32, mut b: Vec<i32>, MOD: i32) -> i32 {
        if b.len() == 0 {
            return 1;
        }
        let c = b.pop().unwrap();
        let head = Solution::super_pow_handler(base, b, MOD);
        return (Solution::pow(head, 10, MOD) * Solution::pow(base, c, MOD)) % MOD;

    }

    pub fn super_pow(a: i32, mut b: Vec<i32>) -> i32 {
        let MOD = 1337;
        return Solution::super_pow_handler(a % MOD, b, MOD);
    }
}
