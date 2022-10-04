// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
//
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }


impl Solution {
    pub fn merge_two_lists(list1: Option<Box<ListNode>>, list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut head = Some(Box::new(ListNode::new(-1)));
        let mut current = head.as_mut().unwrap();
        let mut head1 = list1;
        let mut head2 = list2;

        while head1 != None || head2 != None {
            if head2 == None {
                current.next = head1.clone();
                break;
            }
            if head1 == None {
                current.next = head2.clone();
                break;
            }
            if head1.as_ref().unwrap().val < head2.as_ref().unwrap().val {
                current.next = head1.clone();
                head1 = head1.unwrap().next;
            } else {
                current.next = head2.clone();
                head2 = head2.unwrap().next;
            }
            current = current.next.as_mut().unwrap();
        }
        return head.unwrap().next;
    }
}
