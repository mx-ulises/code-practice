use std::cmp;

impl Solution {
    pub fn minimum_recolors(blocks: String, k: i32) -> i32 {
        let mut count:i32 = 0;
        let mut minimal:i32 = k;
        for i in 0..blocks.len() {
            if k as usize <= i {
                minimal = cmp::min(count, minimal);
            }
            let c:char = blocks.chars().nth(i).unwrap();
            if c == 'W' {
                count += 1;
            }
            if k as usize <= i  {
                let d:char = blocks.chars().nth(i - (k as usize)).unwrap();
                if d == 'W' {
                    count -= 1;
                }
            }
        }
        cmp::min(count, minimal)
    }
}
