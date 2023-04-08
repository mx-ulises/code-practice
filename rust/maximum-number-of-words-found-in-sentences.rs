impl Solution {
    fn built_in_soluton(sentences: Vec<String>) -> i32 {
        let mut maximal_word_count = 0;
        for sentence in sentences {
            let word_count =  sentence.matches(' ').count() + 1;
            maximal_word_count = maximal_word_count.max(word_count);
        }
        return maximal_word_count as i32;
    }

    fn counter_solution(sentences: Vec<String>) -> i32 {
        let mut maximal_word_count = 0;
        for sentence in sentences {
            let mut word_count = 1;
            for c in sentence.chars() {
                if c == ' ' {
                    word_count += 1;
                }
            }
            maximal_word_count = maximal_word_count.max(word_count);
        }
        return maximal_word_count as i32;
    }

    pub fn most_words_found(sentences: Vec<String>) -> i32 {
        return Solution::built_in_soluton(sentences);
    }
}
