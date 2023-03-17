impl Solution {
    pub fn count_asterisks(s: String) -> i32 {
        let mut bar_open = false;
        let mut asterisk_count = 0;
        for c in s.chars() {
            if c == '|' {
                bar_open = bar_open ^ true;
            }
            if c == '*' && !bar_open {
                asterisk_count += 1;
            }
        }
        return asterisk_count;
    }
}
