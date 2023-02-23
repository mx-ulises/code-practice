impl Solution {
    fn get_numeric_value(word: String) -> u32 {
        let mut num = 0;
        for c in word.chars() {
            num = num * 10 + (c as u32 - 97);
        }
        return num;
    }

    pub fn is_sum_equal(first_word: String, second_word: String, target_word: String) -> bool {
        let first_num = Solution::get_numeric_value(first_word);
        let second_num = Solution::get_numeric_value(second_word);
        let target_num = Solution::get_numeric_value(target_word);
        return (first_num + second_num) == target_num;
    }
}
