use std::collections::HashSet;

impl Solution {
    fn getMorseMapping() -> Vec<String> {
        let morse_mapping = vec![".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."];
        let mut output = Vec::new();
        for letter in morse_mapping {
            output.push(letter.to_string());
        }
        return output;
    }

    fn encode(word: String, morse_mapping: &Vec<String>) -> String {
        let mut morse_word_list = Vec::new();
        for c in word.chars() {
            let index = (c as u32) - ('a' as u32);
            morse_word_list.push(morse_mapping[index as usize].to_string());
        }
        return morse_word_list.join("");
    }

    pub fn unique_morse_representations(words: Vec<String>) -> i32 {
        let morse_mapping = Solution::getMorseMapping();
        let mut unique_morse_words = HashSet::new();
        for word in words {
            let morse_word = Solution::encode(word, &morse_mapping);
            unique_morse_words.insert(morse_word);
        }
        return unique_morse_words.len() as i32;
    }
}
