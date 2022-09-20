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
use std::cmp;

impl Solution {
    pub fn find_mode(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut counter = std::collections::HashMap::<i32, i32>::new();
        let mut max = 0;
        let mut s = Vec::new();
        s.push(root);
        while 0 < s.len() {
            match s.pop().unwrap() {
                Some(node) => {
                    *counter.entry(node.borrow().val).or_insert(0) += 1;
                    s.push(node.borrow().left.clone());
                    s.push(node.borrow().right.clone());
                    max = cmp::max(max, counter[&node.borrow().val])
                }
                None => continue,
            }
        }
        let mut modes = Vec::new();
        for (value, count) in &counter {
            if count == &max {
                modes.push(*value);
            }
        }
        return modes;
    }
}
