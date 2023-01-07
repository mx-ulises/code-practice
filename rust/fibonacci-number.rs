impl Solution {
    pub fn fib(n: i32) -> i32 {
        if n == 0 {
            return 0;
        }
        let mut f = 0;
        let mut g = 1;
        for _ in 1..n {
            let x = f + g;
            f = g;
            g = x;
        }
        return g;
    }
}
