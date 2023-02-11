impl Solution {
    fn is_prefix(word: String, prefix: Vec<char>) -> bool {
        if word.len() < prefix.len() {
            return false;
        }
        let word_chars: Vec<char> = word.chars().collect();
        for i in 0..prefix.len() {
            if word_chars[i] != prefix[i] {
                return false;
            }
        }
        return true;
    }

    pub fn is_prefix_of_word(sentence: String, search_word: String) -> i32 {
        let words: Vec<&str> = sentence.split(" ").collect();
        for i in 0..words.len() {
            if Solution::is_prefix(words[i].to_string(), search_word.chars().collect()) {
                return i as i32 + 1;
            }
        }
        return -1;
    }
}
