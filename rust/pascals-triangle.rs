impl Solution {
    pub fn generate(num_rows: i32) -> Vec<Vec<i32>> {
        let mut output:Vec<Vec<i32>> = Vec::new();
        output.push([1].to_vec());
        for i in 1..num_rows as usize{
            let mut row:Vec<i32> = Vec::new();
            row.push(0);
            for j in 0..i {
                row[j] += output[i - 1][j];
                row.push(output[i - 1][j]);
            }
            output.push(row);
        }
        return output
    }
}
