impl Solution {
    pub fn has_alternating_bits(mut n: i32) -> bool {
        let mut previous_bit = n & 1;
        n >>= 1;
        while 0 < n {
            let current_bit = n & 1;
            if current_bit == previous_bit {
                return false;
            }
            previous_bit = current_bit;
            n >>= 1;
        }
        return true;
    }
}
