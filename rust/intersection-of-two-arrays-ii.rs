use std::collections::HashMap;

impl Solution {
    pub fn intersect(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let mut nums1_map = HashMap::new();
        for x in nums1 {
            if !nums1_map.contains_key(&x) {
                nums1_map.insert(x, 0);
            }
            nums1_map.insert(x, nums1_map.get(&x).unwrap() + 1);
        }
        let mut output = Vec::new();
        for x in nums2 {
            if nums1_map.contains_key(&x) && 0 < *(nums1_map.get(&x).unwrap()) {
                nums1_map.insert(x, nums1_map.get(&x).unwrap() - 1);
                output.push(x);
            }
        }
        return output;
    }
}
