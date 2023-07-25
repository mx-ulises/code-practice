/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type TreeNodeBound struct {
	Node  *TreeNode
	Bound int
}

func bstFromPreorder(preorder []int) *TreeNode {
	root := TreeNode{Val: preorder[0]}
	s := make([]TreeNodeBound, 0)
	s = append(s, TreeNodeBound{Node: &root, Bound: 1001})
	for i := 1; i < len(preorder); i++ {
		node := TreeNode{Val: preorder[i]}
		peak := len(s) - 1
		for s[peak].Bound < node.Val {
			s = s[:peak]
			peak -= 1
		}
		parent := s[peak].Node
		bound := s[peak].Bound
		if node.Val < parent.Val {
			parent.Left = &node
			s = append(s, TreeNodeBound{Node: &node, Bound: parent.Val})
		} else {
			parent.Right = &node
			s = append(s, TreeNodeBound{Node: &node, Bound: bound})
		}
	}
	return &root
}
