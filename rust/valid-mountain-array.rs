impl Solution {
    pub fn valid_mountain_array(arr: Vec<i32>) -> bool {
        let mut peak_achieved = false;
        if arr.len() < 3 {
            return false;
        }
        for i in 1..arr.len() {
            if arr[i - 1] < arr[i] && peak_achieved {
                return false;
            }
            else if arr[i - 1] == arr[i] {
                return false;
            }
            else if arr[i] < arr[i - 1] {
                if i == 1 {
                    return false;
                }
                peak_achieved = true;
            }
        }
        return peak_achieved;
    }
}
