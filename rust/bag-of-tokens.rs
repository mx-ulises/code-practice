impl Solution {
    pub fn bag_of_tokens_score(mut tokens: Vec<i32>, mut power: i32) -> i32 {
        if tokens.len() == 0 {
            return 0;
        }
        let mut score = 0;
        tokens.sort();
        let mut i = 0;
        let mut j = tokens.len() - 1;
        while i != j {
            if tokens[i] <= power {
                power -= tokens[i];
                i += 1;
                score += 1;
            } else if 0 < score {
                power += tokens[j];
                j -= 1;
                score -= 1;
            } else {
                break;
            }
        }
        if tokens[i] <= power {
            power -= tokens[i];
            i += 1;
            score += 1;
        }
        return score;
    }
}
