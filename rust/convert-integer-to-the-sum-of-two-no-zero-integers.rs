impl Solution {
    fn is_not_zero_integer(mut a: i32) -> bool {
        while a != 0 {
            if a % 10 == 0 {
                return false;
            }
            a = a / 10;
        }
        return true;
    }

    pub fn get_no_zero_integers(n: i32) -> Vec<i32> {
        let mut output = Vec::new();
        for a in 1..n {
            let b = n - a;
            //println!("a: {}, b: {}", a, b);
            if Solution::is_not_zero_integer(a) && Solution::is_not_zero_integer(b) {
                output.push(a);
                output.push(b);
                break;
            }
        }
        return output
    }
}
