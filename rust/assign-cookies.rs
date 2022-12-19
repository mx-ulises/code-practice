impl Solution {
    pub fn find_content_children(mut g: Vec<i32>,mut s: Vec<i32>) -> i32 {
        let mut content_children = 0;
        g.sort();
        s.sort();
        for cookie in s {
            if content_children < g.len() && g[content_children] <= cookie {
                content_children += 1;
            }
        }
        return content_children as i32;
    }
}
