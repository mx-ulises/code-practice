/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */


 func pairSum(head *ListNode) int {
    current := head
    runner := head
    var prev *ListNode = nil
    for runner != nil {
        runner = runner.Next.Next
        aux := current.Next
        current.Next = prev
        prev = current
        current = aux
    }
    maximal := 0
    for current != nil {
        sum := current.Val + prev.Val
        if maximal < sum {
            maximal = sum
        }
        current = current.Next
        prev = prev.Next
    }
    return maximal
}
