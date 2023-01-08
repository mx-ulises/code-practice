use std::collections::HashSet;

impl Solution {
    fn find_next(mut n: i32) -> i32 {
        let mut next_n = 0;
        while 0 < n  {
            let d = n % 10;
            next_n += d * d;
            n = n / 10;
        }
        return next_n;
    }

    fn solution_hashset(mut n: i32) -> bool {
        let mut visited_numbers = HashSet::new();
        while n != 1 {
            if visited_numbers.contains(&n) {
                return false;
            }
            visited_numbers.insert(n);
            n = Solution::find_next(n);
        }
        return true;
    }

    fn solution_loop_finder(mut n: i32) -> bool {
        let mut current = n;
        let mut runner = Solution::find_next(n);
        while runner != 1 && runner != current {
            current = Solution::find_next(current);
            runner = Solution::find_next(Solution::find_next(runner));
        }
        return runner == 1;
    }

    pub fn is_happy(mut n: i32) -> bool {
        return Solution::solution_loop_finder(n);
    }
}
