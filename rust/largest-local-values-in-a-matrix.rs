impl Solution {
    fn get_local_maximal(grid: &Vec<Vec<i32>>, x: usize, y: usize) -> i32 {
        let mut maximal = 0;
        for i in 0..3 {
            for j in 0..3 {
                maximal = maximal.max(grid[x + i][y + j]);
            }
        }
        return maximal;
    }

    pub fn largest_local(grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut new_grid = Vec::new();
        let n = grid.len() - 2;
        let m = grid[0].len() - 2;
        for x in 0..n {
            let mut row = Vec::new();
            for y in 0..m {
                let maximal = Solution::get_local_maximal(&grid, x, y);
                row.push(maximal);
            }
            new_grid.push(row);
        }
        return new_grid;
    }
}
