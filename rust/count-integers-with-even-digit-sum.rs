impl Solution {
    fn is_even_digit_sum(mut x: i32) -> bool {
        let mut output = 0;
        while x != 0 {
            output ^= x;
            x /= 10;
        }
        return output & 1 == 0;
    }

    pub fn count_even(num: i32) -> i32 {
        let mut count = 0;
        for x in 1..(num + 1) {
            if Solution::is_even_digit_sum(x) {
                count += 1;
            }
        }
        return count;
    }
}
