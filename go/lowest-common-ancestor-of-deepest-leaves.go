/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func GetLCADepestLeaves(node *TreeNode, level int) (*TreeNode, int) {
	if node == nil {
		return node, level
	}
	nodeLeft, depthLeft := GetLCADepestLeaves(node.Left, level+1)
	nodeRight, depthRight := GetLCADepestLeaves(node.Right, level+1)
	depth := depthLeft
	if depthLeft < depthRight {
		node = nodeRight
		depth = depthRight
	}
	if depthRight < depthLeft {
		node = nodeLeft
		depth = depthLeft
	}
	return node, depth
}

func lcaDeepestLeaves(root *TreeNode) *TreeNode {
	node, _ := GetLCADepestLeaves(root, 0)
	return node
}
