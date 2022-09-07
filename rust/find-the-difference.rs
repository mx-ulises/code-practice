use std::collections::HashMap;
use std::iter::FromIterator;

impl Solution {

    pub fn find_the_difference(s: String, t: String) -> char {
        // Initialize HashMap where character count will be held
        let mut char_count:HashMap<char,u32> = HashMap::new();

        // Iterate over s and increase the count by one for each char found
        for c in s.chars() {
            match char_count.get(&c) {
                Some(count) => char_count.insert(c, count + 1),
                None => char_count.insert(c, 1)
            };
        }

        // Iterate over t and find the missing element, or decrease the count
        for c in t.chars() {
            match char_count.get(&c) {
                Some(0) => return c,
                None => return c,
                Some(count) => char_count.insert(c, count - 1)
            };
        }

        // Default scenario with zero
        '0'
    }
}
