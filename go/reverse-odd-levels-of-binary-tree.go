/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func reverseLevel(q []*TreeNode, n int) []*TreeNode {
	for i := 0; i < (n / 2); i++ {
		j := n - i - 1
		aux := q[i].Val
		q[i].Val = q[j].Val
		q[j].Val = aux
	}
	return q
}

func addNode(q []*TreeNode, node *TreeNode) []*TreeNode {
	if node != nil {
		q = append(q, node)
	}
	return q
}

func reverseOddLevels(root *TreeNode) *TreeNode {
	q := make([]*TreeNode, 0)
	q = append(q, root)
	level := 0
	for 0 < len(q) {
		n := len(q)
		if level&1 == 1 {
			q = reverseLevel(q, n)
		}
		for i := 0; i < n; i++ {
			node := q[0]
			q = q[1:]
			q = addNode(q, node.Left)
			q = addNode(q, node.Right)
		}
		level += 1
	}
	return root
}
