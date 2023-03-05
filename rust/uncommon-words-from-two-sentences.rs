use std::collections::HashMap;

impl Solution {
    pub fn uncommon_from_sentences(s1: String, s2: String) -> Vec<String> {
        let mut word_count = HashMap::new();
        for word in s1.split(" ") {
            *word_count.entry(word).or_insert(0) += 1;
        }
        for word in s2.split(" ") {
            *word_count.entry(word).or_insert(0) += 1;
        }
        let mut output = Vec::new();
        for (word, count) in word_count.into_iter() {
            if count == 1 {
                output.push(word.to_owned())
            }
        }
        return output
    }
}
