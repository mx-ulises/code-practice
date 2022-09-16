use std::cmp;

impl Solution {
    pub fn distribute_candies(candies: i32, num_people: i32) -> Vec<i32> {
        let mut output = vec![0; num_people as usize];
        let mut i:i32 = 0;
        let mut available_candies:i32 = candies;
        while 0 < available_candies {
            output[(i%num_people) as usize] += std::cmp::min(available_candies, i + 1);
            i += 1;
            available_candies -= i;
        }
        return output;
    }
}
