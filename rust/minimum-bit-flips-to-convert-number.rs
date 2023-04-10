impl Solution {
    pub fn min_bit_flips(start: i32, goal: i32) -> i32 {
        let mut flips = start ^ goal;
        let mut flip_count = 0;
        while 0 < flips {
            if flips & 1 == 1 {
                flip_count += 1;
            }
            flips = flips >> 1;
        }
        return flip_count;
    }
}
