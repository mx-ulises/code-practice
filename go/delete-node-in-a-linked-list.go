/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

 func CopyValues(node *ListNode) {
    node.Val = node.Next.Val
    node.Next = node.Next.Next
}

func CopyMemAddr(node *ListNode) {
    *node = *node.Next
}

func deleteNode(node *ListNode) {
    CopyMemAddr(node)
}
