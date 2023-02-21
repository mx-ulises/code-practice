impl Solution {
    pub fn find_the_array_conc_val(nums: Vec<i32>) -> i64 {
        let mut concatenation_value = 0;
        let (mut i, mut j) = (0, nums.len() - 1);
        while i < j {
            let power = (nums[j] as f64).log10().floor() as u32 + 1;
            let multiplier = (10 as i64).pow(power);
            concatenation_value += (nums[i] as i64) * multiplier + (nums[j] as i64);
            i += 1;
            j -= 1;
        }
        if i == j {
            concatenation_value += nums[i] as i64;
        }
        return concatenation_value;
    }
}
