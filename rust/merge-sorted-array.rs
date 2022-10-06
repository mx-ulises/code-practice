impl Solution {
    pub fn merge(nums1: &mut Vec<i32>, m: i32, nums2: &mut Vec<i32>, n: i32) {
        let mut i_1 = m as usize;
        let mut i_2 = n as usize;
        while 0 < i_1 || 0 < i_2 {
            let j = i_1 + i_2 - 1;
            if i_1 == 0 {
                i_2 -= 1;
                nums1[j] = nums2[i_2];
            } else if i_2 == 0 {
                i_1 -= 1;
                nums1[j] = nums1[i_1];
            } else if nums1[i_1 - 1] < nums2[i_2 - 1] {
                i_2 -= 1;
                nums1[j] = nums2[i_2];
            } else {
                i_1 -= 1;
                nums1[j] = nums1[i_1];
            }
        }
    }
}
