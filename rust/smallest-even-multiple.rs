impl Solution {
    pub fn smallest_even_multiple(n: i32) -> i32 {
        if n & 1 == 1 {
            return n << 1;
        }
        return n;
    }
}
