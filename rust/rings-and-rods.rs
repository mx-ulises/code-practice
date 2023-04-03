use std::collections::HashMap;

impl Solution {
    pub fn count_points(rings: String) -> i32 {
        let mut colors_in_rod = HashMap::new();
        let mut color = 'E';
        for c in rings.chars() {
            match color {
                'R' => *colors_in_rod.entry(c).or_insert(0) |= 1,
                'G' => *colors_in_rod.entry(c).or_insert(0) |= 2,
                'B' => *colors_in_rod.entry(c).or_insert(0) |= 4,
                _  => color = c
            }
            color = c;
        }
        let mut points = 0;
        for (key, colors) in colors_in_rod {
            if colors == 7 {
                points += 1;
            }
        }
        return points;
    }
}
