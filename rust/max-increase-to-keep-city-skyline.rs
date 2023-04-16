impl Solution {
    pub fn max_increase_keeping_skyline(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let m = grid[0].len();
        let mut row_maxes = vec![0; n];
        let mut col_maxes = vec![0; m];
        for i in 0..n {
            for j in 0..m {
                row_maxes[i] = row_maxes[i].max(grid[i][j]);
                col_maxes[j] = col_maxes[j].max(grid[i][j]);
            }
        }
        let mut heigh_diff = 0;
        for i in 0..n {
            for j in 0..m {
                heigh_diff += row_maxes[i].min(col_maxes[j]) - grid[i][j];
            }
        }
        return heigh_diff;
    }
}
