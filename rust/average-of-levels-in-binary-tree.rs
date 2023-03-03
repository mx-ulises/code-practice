// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }

use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn average_of_levels(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<f64> {
        let mut averages = Vec::new();
        let mut dq = std::collections::VecDeque::new();
        dq.push_back(root);
        while !dq.is_empty() {
            let mut s = 0.0;
            let mut n = 0.0;
            for _ in 0..dq.len() {
                if let Some(Some(node)) = dq.pop_front() {
                    let node = node.borrow();
                    s += node.val as f64;
                    n += 1.0;
                    dq.push_back(node.left.clone());
                    dq.push_back(node.right.clone());
                }
            }
            if 0.0 < n {
                averages.push(s / n);
            }
        }
        return averages
    }
}
