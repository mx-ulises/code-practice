impl Solution {
    pub fn judge_circle(moves: String) -> bool {
        let mut x:i32 = 0;
        for c in moves.chars() {
            match c {
                'U' => x += 1,
                'D' => x -= 1,
                'L' => x += 100000,
                _ => x -= 100000
            }
        }
        return x == 0;
    }
}
