impl Solution {
    pub fn watering_plants(plants: Vec<i32>, capacity: i32) -> i32 {
        let mut steps = 0;
        let mut bucket = capacity;
        for i in 0..plants.len() {
            if bucket < plants[i] {
                steps += (i * 2) as i32;
                bucket = capacity;
            }
            bucket -= plants[i];
            steps += 1;
        }
        return steps;
    }
}
