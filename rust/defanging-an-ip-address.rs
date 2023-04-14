use std::iter::FromIterator;

impl Solution {
    pub fn defang_i_paddr(address: String) -> String {
        let mut defang_address = vec![];
        for c in address.chars() {
            if c == '.' {
                defang_address.push('[');
            }
            defang_address.push(c);
            if c == '.' {
                defang_address.push(']');
            }
        }
        return String::from_iter(defang_address);
    }
}
