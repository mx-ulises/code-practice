impl Solution {
    pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
        let mut n = matrix.len() - 1;
        let mut offset = 0;
        while offset < n {
            for i in 0..(n - offset) {
                let aux = matrix[offset + i][n];
                matrix[offset + i][n] = matrix[offset][offset + i];
                matrix[offset][offset + i] = matrix[n - i][offset];
                matrix[n - i][offset] = matrix[n][n - i];
                matrix[n][n - i] = aux;
            }
            offset += 1;
            n -= 1
        }
    }
}
