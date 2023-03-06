impl Solution {
    pub fn find_kth_positive(arr: Vec<i32>, mut k: i32) -> i32 {
        let mut prev = 0;
        for x in arr {
            let delta = x - prev - 1;
            if k <= delta {
                break;
            }
            k -= delta;
            prev = x;
        }
        return prev + k;
    }
}
