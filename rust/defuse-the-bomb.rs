impl Solution {
    pub fn decrypt(code: Vec<i32>, k: i32) -> Vec<i32> {
        let start;
        if k < 0 {
            start = (code.len() as i32 + k) as usize;
        } else {
            start = 1;
        }
        let end = (start + (k.abs() as usize));
        let mut sum = 0;
        for i in start..end {
            sum += code[i % code.len()];
        }
        let mut decode = Vec::new();
        for i in 0..code.len() {
            decode.push(sum);
            let j = (start + i) % code.len();
            let k = (end + i) % code.len();
            sum += code[k] - code[j];
        }
        return decode;
    }
}
