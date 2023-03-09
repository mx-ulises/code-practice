impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let mut left = 0;
        let mut right = nums.len() as i32 - 1;
        while left <= right {
            let mid = (left + right) / 2;
            if target == nums[mid as usize] {
                return mid;
            } else if target < nums[mid as usize] {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return -1;
    }
}
