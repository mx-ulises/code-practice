impl Solution {
    pub fn check_perfect_number(num: i32) -> bool {
        if num == 1 {
            return false;
        }
        let mut output:i32 = 1;
        let mut left:i32 = 2;
        let mut right:i32 = num/2;
        while left <= right {
            if num % left == 0 {
                output += left;
                if left != right {
                    output += right;
                }
                if num < output {
                    return false;
                }
            }
            left += 1;
            right = num / left;
        }
        return num == output
    }
}
