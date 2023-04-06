impl Solution {
    pub fn min_operations(boxes: String) -> Vec<i32> {
        let mut left_count = 0;
        let mut left_moves = 0;
        let mut right_count = 0;
        let mut right_moves = 0;
        let mut operations = Vec::new();
        for i in 1..boxes.len(){
            if boxes.chars().nth(i).unwrap() == '1' {
                right_count += 1;
                right_moves += i as i32;
            }
        }
        operations.push(left_moves + right_moves);
        for i in 1..boxes.len(){
            if boxes.chars().nth(i - 1).unwrap() == '1' {
                left_count += 1;
            }
            left_moves += left_count;
            right_moves -= right_count;
            if boxes.chars().nth(i).unwrap() == '1' {
                right_count -= 1;
            }
            operations.push(left_moves + right_moves);
        }
        return operations;
    }
}
