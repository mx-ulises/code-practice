use std::collections::HashMap;

impl Solution {
    pub fn can_be_equal(target: Vec<i32>, arr: Vec<i32>) -> bool {
        let mut char_count: HashMap<i32,i32> = HashMap::new();
        for x in target {
            if !char_count.contains_key(&x) {
                char_count.insert(x, 0);
            }
            let v = char_count.get(&x).unwrap() + 1;
            char_count.insert(x, v);
        }
        for x in arr {
            if !char_count.contains_key(&x) || *char_count.get(&x).unwrap() == 0 {
                return false;
            }
            let v = char_count.get(&x).unwrap() - 1;
            char_count.insert(x, v);
        }
        return true;
    }
}
