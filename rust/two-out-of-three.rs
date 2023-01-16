use std::collections::HashSet;

impl Solution {
    pub fn two_out_of_three(nums1: Vec<i32>, nums2: Vec<i32>, nums3: Vec<i32>) -> Vec<i32> {
        let nums1_set:HashSet<i32> = nums1.into_iter().collect();
        let nums2_set:HashSet<i32> = nums2.into_iter().collect();
        let nums3_set:HashSet<i32> = nums3.into_iter().collect();
        let mut nums4_set = HashSet::new();
        for x in nums1_set {
            if nums2_set.contains(&x) || nums3_set.contains(&x) {
                nums4_set.insert(x);
            }
        }
        for x in nums2_set {
            if nums3_set.contains(&x) {
                nums4_set.insert(x);
            }
        }
        return nums4_set.into_iter().collect();
    }
}
