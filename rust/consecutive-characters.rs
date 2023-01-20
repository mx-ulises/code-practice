use std::cmp;

impl Solution {
    pub fn max_power(s: String) -> i32 {
        let mut current = 'a';
        let mut current_power = 0;
        let mut max_power = 0;
        for c in s.chars() {
            if current == c {
                current_power += 1;
                max_power = cmp::max(current_power, max_power);
            } else {
                current = c;
                current_power = 1;
            }
        }
        return cmp::max(current_power, max_power);
    }
}
