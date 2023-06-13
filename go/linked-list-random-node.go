/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

type Solution struct {
	NodeValues []int
}

func Constructor(head *ListNode) Solution {
	current := head
	nodeValues := make([]int, 0)
	for current != nil {
		nodeValues = append(nodeValues, current.Val)
		current = current.Next
	}
	return Solution{NodeValues: nodeValues}
}

func (this *Solution) GetRandom() int {
	i := rand.Intn(len(this.NodeValues))
	return this.NodeValues[i]
}

/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(head);
 * param_1 := obj.GetRandom();
 */
