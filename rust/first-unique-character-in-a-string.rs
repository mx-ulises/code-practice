use std::collections::HashMap;

impl Solution {
    pub fn first_uniq_char(s: String) -> i32 {
        let mut char_count = HashMap::new();
        for c in s.chars() {
            *char_count.entry(c).or_insert(0) += 1;
        }
        let mut i = 0;
        for c in s.chars() {
            if char_count[&c] == 1 {
                return i;
            }
            i += 1;
        }
        return -1
    }
}
