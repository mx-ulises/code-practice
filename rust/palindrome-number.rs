impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if x < 0 {
            return false;
        }
        if x == 0 {
            return true;
        }
        let mut log10 = x.log(10) as i32;
        let mut num = x;
        while 1 < log10 {
            let msd = num / log10;
            let lsd = num % 10;
            if msd != lsd {
                return false
            }
            num = (num - lsd - (msd * log10)) / 10;
            log10 = log10 / 100;
        }
        return true
    }

    pub fn is_palindrome_2(x: i32) -> bool {
        if(x < 0 || (x % 10 == 0 && x != 0)) {
            return false
        }
        let mut num = x;
        let mut rev_num = 0;
        while rev_num < num {
            rev_num = rev_num * 10 + (num % 10);
            num /= 10;
        }
        return rev_num == num || (rev_num / 10) == num
    }
}
