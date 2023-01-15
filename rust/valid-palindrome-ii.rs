impl Solution {
    pub fn valid_palindrome(s: String) -> bool {
        let mut i = 0;
        let mut j = s.len() - 1;
        let mut deleted = 0;
        // Try remove right
        let chars = s.as_bytes();
        while i < j {
            if chars[i] != chars[j] {
                deleted += 1;
                if 1 < deleted {
                    break;
                }
            } else {
                i += 1;
            }
            j -= 1;
        }
        if deleted < 2 {
            return true;
        }
        // Try remove left
        i = 0;
        j = s.len() - 1;
        deleted = 0;
        while i < j {
            if chars[i] != chars[j] {
                deleted += 1;
                if 1 < deleted {
                    break;
                }
            } else {
                j -= 1;
            }
            i += 1;
        }
        return deleted < 2
    }
}
