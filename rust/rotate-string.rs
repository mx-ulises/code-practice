impl Solution {
    pub fn rotate_string(s: String, goal: String) -> bool {
       let ss = format!("{}{}", s.to_owned(), s.to_owned());
        return s.len() == goal.len() && ss.contains(&goal);
    }
}
