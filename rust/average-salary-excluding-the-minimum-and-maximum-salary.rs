use std::cmp;

impl Solution {
    pub fn average(salary: Vec<i32>) -> f64 {
        let mut min:i32 = *salary.iter().min().unwrap();
        let mut max:i32 = *salary.iter().max().unwrap();
        let mut sum:i32 = salary.iter().sum();
        let n:usize = salary.len() - 2;
        return ((sum - min - max) as f64) / (n as f64);
    }
}
