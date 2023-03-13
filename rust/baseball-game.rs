impl Solution {
    pub fn cal_points(operations: Vec<String>) -> i32 {
        let mut records = Vec::new();
        for operation in operations {
            if operation == "C" {
                records.pop();
            } else if operation == "D" {
                records.push(records[records.len() - 1] * 2);
            } else if operation == "+" {
                records.push(records[records.len() - 1] + records[records.len() - 2]);
            } else {
                records.push(operation.parse().unwrap());
            }
        }
        return records.iter().sum();
    }
}
