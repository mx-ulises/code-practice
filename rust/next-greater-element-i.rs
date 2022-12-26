use std::collections::HashMap;

impl Solution {
    pub fn next_greater_element(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let mut s = Vec::new();
        let mut next_element = HashMap::new();
        for x in nums2 {
            while 0 < s.len() && s[s.len() - 1] < x {
                next_element.insert(s.pop().unwrap(), x);
            }
            s.push(x);
        }
        while 0 < s.len() {
            next_element.insert(s.pop().unwrap(), -1);
        }
        let mut output = Vec::new();
        for x in nums1 {
            output.push(*next_element.get(&x).unwrap());
        }
        return output;
    }
}
