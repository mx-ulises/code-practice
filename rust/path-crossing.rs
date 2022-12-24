use std::collections::HashMap;
use std::collections::HashSet;

impl Solution {
    pub fn is_path_crossing(path: String) -> bool {
        let DIRECTIONS = HashMap::from([
            ('N', 100000),
            ('S', -100000),
            ('E', 1),
            ('W', -1)
        ]);
        let mut current_position = 0;
        let mut visited = HashSet::new();
        visited.insert(current_position);
        for c in path.chars() {
            current_position += DIRECTIONS[&c];
            if visited.contains(&current_position) {
                return true;
            }
            visited.insert(current_position);
        }
        return false;
    }
}
