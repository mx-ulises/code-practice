impl Solution {
    pub fn add_digits(mut num: i32) -> i32 {
        while 10 <= num {
            let mut new_num = 0;
            while 0 < num {
                new_num += num % 10;
                num = num / 10;
            }
            num = new_num;
        }
        return num;
    }
}
