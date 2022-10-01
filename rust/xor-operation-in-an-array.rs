impl Solution {
    pub fn xor_operation(n: i32, start: i32) -> i32 {
        let mut out = 0;
        for i in 0..n {
            out ^= (start + 2 * i);
        }
        return out
    }
}
