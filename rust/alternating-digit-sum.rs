impl Solution {
    pub fn alternate_digit_sum(mut n: i32) -> i32 {
        let mut odd_sum = 0;
        let mut even_sum = 0;
        let mut digit_count = 0;
        while 0 < n {
            digit_count += 1;
            if digit_count & 1 == 1 {
                odd_sum += n % 10;
            } else {
                even_sum += n % 10;
            }
            n = n / 10;
        }
        if digit_count & 1 == 1 {
            return odd_sum - even_sum;
        }
        return even_sum - odd_sum;
    }
}
