impl Solution {
    pub fn replace_digits(s: String) -> String {
        let mut t = String::from("");
        let mut prev_c = 'a';
        for (i, c) in s.chars().enumerate() {
            if i % 2 == 0 {
                t.push(c);
            } else {
                let d = c as u32 + prev_c as u32 - '0' as u32;
                t.push(char::from_u32(d).unwrap())
            }
            prev_c = c;
        }
        return t;
    }
}
