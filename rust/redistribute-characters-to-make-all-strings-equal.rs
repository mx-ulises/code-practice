use std::collections::HashMap;

impl Solution {
    pub fn make_equal(words: Vec<String>) -> bool {
        let mut char_count = HashMap::new();
        let n = words.len();
        for word in words {
            for c in word.chars() {
                char_count.entry(c).and_modify(|e| { *e += 1 }).or_insert(1);
            }
        }
        for (_, count) in char_count {
            if count % n != 0 {
                return false;
            }
        }
        return true;
    }
}
