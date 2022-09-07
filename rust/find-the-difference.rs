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

    fn get_char_sum(s: String) -> u32 {
        let mut sum:u32 = 0;
        for c in s.chars() {
            sum += &c.into();
        }
        return sum
    }

    pub fn find_the_difference_2(s: String, t: String) -> char {
        let s_sum:u32 = Solution::get_char_sum(s);
        let t_sum:u32 = Solution::get_char_sum(t);
        return (t_sum - s_sum).try_into().unwrap()
    }
}
