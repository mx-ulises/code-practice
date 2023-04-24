impl Solution {
    fn get_distance(point: &Vec<i32>, circle: &Vec<i32>) -> i32 {
        let term1 = point[0] - circle[0];
        let term2 = term1 * term1;
        let term3 = point[1] - circle[1];
        let term4 = term3 * term3;
        return term2 + term4;
    }

    pub fn count_points(points: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let mut answer = Vec::new();
        for circle in queries {
            let i = answer.len();
            answer.push(0);
            for j in 0..points.len() {
                let d = Solution::get_distance(&points[j], &circle);
                let r = circle[2] * circle[2];
                if d <= r {
                    answer[i] += 1;
                }
            }
        }
        return answer;
    }
}
