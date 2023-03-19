impl Solution {
    pub fn sort_array_by_parity_ii(mut nums: Vec<i32>) -> Vec<i32> {
        let mut even_i = 0;
        let mut odd_i = 1;
        let n = nums.len();
        while even_i < n && odd_i < n {
            if nums[even_i] & 1 == 1 && nums[odd_i] & 1 == 0 {
                let aux = nums[even_i];
                nums[even_i] = nums[odd_i];
                nums[odd_i] = aux;
            }
            if nums[even_i] & 1 == 0 {
                even_i += 2;
            }
            if nums[odd_i] & 1 == 1 {
                odd_i += 2;
            }
        }
        return nums;
    }
}
