impl Solution {
    pub fn alternate_digit_sum(mut n: i32) -> i32 {
        let mut alternate_sum = 0;
        let mut digit_count = 0;
        while 0 < n {
            digit_count ^= 1;
            if digit_count & 1 == 0 {
                alternate_sum += n % 10;
            } else {
                alternate_sum -= n % 10;
            }
            n = n / 10;
        }
        if digit_count & 1 == 1 {
            alternate_sum = -alternate_sum;
        }
        return alternate_sum
    }
}
