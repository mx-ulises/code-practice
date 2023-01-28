impl Solution {
    pub fn count_segments(s: String) -> i32 {
        let mut segment_count = 0;
        let mut prev = ' ';
        for c in s.chars() {
            if c == ' ' && prev != ' ' {
                segment_count += 1;
            }
            prev = c;
        }
        if prev != ' ' {
            segment_count += 1;
        }
        return segment_count;
    }
}
