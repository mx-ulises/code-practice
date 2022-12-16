impl Solution {
    pub fn get_row(row_index: i32) -> Vec<i32> {
        let mut row: Vec<i32> = vec![1];
        for i in 1..(row_index + 1) as usize {
            let mut new_row: Vec<i32> = vec![0];
            for j in 0..i {
                new_row[j] += row[j];
                new_row.push(row[j]);
            }
            row = new_row;
        }
        return row;
    }
}
