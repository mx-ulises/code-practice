/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

 func ConstructTree(node *TreeNode, newNode *TreeNode) {
    if node.Right == nil {
        node.Right = newNode
    } else if node.Right.Val < newNode.Val {
        newNode.Left = node.Right
        node.Right = newNode
    } else {
        ConstructTree(node.Right, newNode)
    }
}

func insertIntoMaxTree(root *TreeNode, val int) *TreeNode {
    newNode := TreeNode{
        Val: val,
    }
    if root == nil {
        return &newNode
    }
    if root.Val < newNode.Val {
        newNode.Left = root
        return &newNode
    }
    ConstructTree(root, &newNode)
    return root
}
