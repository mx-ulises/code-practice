impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut count:i32 = 0;
        let mut candidate:i32 = -1;
        for x in nums {
            if count == 0 {
                candidate = x;
            }
            if x == candidate {
                count += 1;
            } else {
                count -= 1;
            }
        }
        return candidate;
    }
}