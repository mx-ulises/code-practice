/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

 func insert(node *TreeNode, val int) {
    if val < node.Val {
        if node.Left == nil {
            node.Left = &TreeNode{Val: val}
        } else {
            insert(node.Left, val)
        }
    } else {
        if node.Right == nil {
            node.Right = &TreeNode{Val: val}
        } else {
            insert(node.Right, val)
        }
    }
}

func insertIntoBST(root *TreeNode, val int) *TreeNode {
    if root == nil {
        root = &TreeNode{Val: val}
    } else {
        insert(root, val)
    }
    return root
}
