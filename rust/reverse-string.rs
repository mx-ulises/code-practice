impl Solution {
    pub fn reverse_string(s: &mut Vec<char>) {
        for i in 0..(s.len() / 2) {
            let j = s.len() - i - 1;
            let c = s[i];
            s[i] = s[j];
            s[j] = c;
        }
    }
}
