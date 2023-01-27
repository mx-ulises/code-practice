use std::collections::HashMap;

impl Solution {
    fn get_rank(a: usize) -> String {
        match a {
            1 => "Gold Medal".to_string(),
            2 => "Silver Medal".to_string(),
            3 => "Bronze Medal".to_string(),
            _ => a.to_string()
        }
    }

    pub fn find_relative_ranks(mut score: Vec<i32>) -> Vec<String> {
        let mut map = HashMap::new();
        for i in 0..score.len() {
            map.insert(score[i], i);
        }
        score.sort();
        let mut answer = vec!["".to_string(); score.len()];
        for i in 0..score.len() {
            let j = score.len() - i - 1;
            answer[map[&score[j]]] = Solution::get_rank(i + 1);
        }
        return answer;
    }
}
