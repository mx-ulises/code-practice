impl Solution {
    pub fn is_one_bit_character(bits: Vec<i32>) -> bool {
        let mut i = 0;
        let mut is_one_bit = false;
        while i < bits.len() {
            if bits[i] == 1 {
                i += 2;
                is_one_bit = false;
            } else {
                i += 1;
                is_one_bit = true;
            }
        }
        return is_one_bit;
    }
}
