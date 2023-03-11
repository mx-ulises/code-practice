use std::cmp;

impl Solution {
    pub fn maximum_wealth(accounts: Vec<Vec<i32>>) -> i32 {
        let mut maximal = 0;
        for customer in accounts {
            let sum: i32 = customer.iter().sum();
            maximal = cmp::max(sum, maximal);
        }
        return maximal
    }
}
