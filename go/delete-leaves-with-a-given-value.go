/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

 func RemoveLeaves(node *TreeNode, target int) *TreeNode {
    if node == nil {
        return nil
    }
    node.Left = RemoveLeaves(node.Left, target)
    node.Right = RemoveLeaves(node.Right, target)
    if node.Left == nil && node.Right == nil && node.Val == target {
        return nil
    }
    return node
}

func removeLeafNodes(root *TreeNode, target int) *TreeNode {
    return RemoveLeaves(root, target)
}
