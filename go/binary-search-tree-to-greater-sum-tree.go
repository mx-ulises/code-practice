/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func BstToGst(node *TreeNode, sum int) int {
	if node == nil {
		return sum
	}
	node.Val += BstToGst(node.Right, sum)
	return BstToGst(node.Left, node.Val)
}

func bstToGst(root *TreeNode) *TreeNode {
	BstToGst(root, 0)
	return root
}
