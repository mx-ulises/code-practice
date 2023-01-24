impl Solution {
    pub fn is_circular_sentence(sentence: String) -> bool {
        let char_vector:Vec<char> = sentence.chars().collect();
        for i in 1..char_vector.len() {
            if char_vector[i] == ' ' && char_vector[i - 1] != char_vector[i + 1] {
                return false;
            }
        }
        return char_vector[0] == char_vector[char_vector.len() - 1];
    }
}
