impl Solution {
    pub fn subtract_product_and_sum(mut n: i32) -> i32 {
        if n == 0 {
            return 0;
        }
        let mut summatory = 0;
        let mut product = 1;
        while 0 < n {
            let d = n % 10;
            n = n / 10;
            summatory += d;
            product *= d;
        }
        return product - summatory;
    }
}
