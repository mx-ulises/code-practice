/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func getDeepestSubtree(node *TreeNode, level int) (*TreeNode, int) {
	if node == nil {
		return node, level
	}
	newLevel := level + 1
	nodeLeft, levelLeft := getDeepestSubtree(node.Left, newLevel)
	nodeRight, levelRight := getDeepestSubtree(node.Right, newLevel)
	if levelLeft < levelRight {
		return nodeRight, levelRight
	} else if levelRight < levelLeft {
		return nodeLeft, levelLeft
	}
	return node, levelLeft
}

func subtreeWithAllDeepest(root *TreeNode) *TreeNode {
	node, _ := getDeepestSubtree(root, 0)
	return node
}
