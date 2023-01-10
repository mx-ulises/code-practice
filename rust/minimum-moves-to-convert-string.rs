impl Solution {
    pub fn minimum_moves(s: String) -> i32 {
        let mut i = 0;
        let mut move_count = 0;
        while i < s.len() {
            if s.chars().nth(i).unwrap() == 'X' {
                move_count += 1;
                i += 3;
            } else {
                i += 1;
            }
        }
        return move_count;
    }
}
