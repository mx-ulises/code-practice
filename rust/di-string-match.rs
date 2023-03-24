impl Solution {
    pub fn di_string_match(s: String) -> Vec<i32> {
        let mut output = Vec::new();
        let mut min = 0;
        let mut max = s.len() as i32;
        for c in s.chars() {
            if c == 'I' {
                output.push(min);
                min += 1;
            } else {
                output.push(max);
                max -= 1;
            }
        }
        output.push(min);
        return output;
    }
}
