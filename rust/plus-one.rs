impl Solution {
    pub fn plus_one(digits: Vec<i32>) -> Vec<i32> {
        let mut output = Vec::new();
        let mut carry = 1;
        for i in 0..digits.len() {
            let d = digits[digits.len() - i - 1];
            let x = (d + carry) % 10;
            carry = (d + carry) / 10;
            output.push(x);
        }
        if carry == 1 {
            output.push(1)
        }
        return output.into_iter().rev().collect();
    }
}
