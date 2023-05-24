/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

 type TreeNodeLevel struct {
    Level int
    Node *TreeNode
}

func CreateTreeNodeLevel(node *TreeNode, level int) *TreeNodeLevel {
    var treeNodeLevel TreeNodeLevel
    treeNodeLevel.Level = level
    treeNodeLevel.Node = node
    return &treeNodeLevel
}

func findBottomLeftValue(root *TreeNode) int {
    stack := make([]*TreeNodeLevel, 0)
    stack = append(stack, CreateTreeNodeLevel(root, 0))
    var bottomLeftValue int
    level := -1
    for 0 < len(stack) {
        treeNodeLevel := stack[0]
        stack = stack[1:]
        if treeNodeLevel.Node == nil {
            continue
        }
        if level < treeNodeLevel.Level {
            level = treeNodeLevel.Level
            bottomLeftValue = treeNodeLevel.Node.Val
        }
        next_level := treeNodeLevel.Level + 1
        stack = append(stack, CreateTreeNodeLevel(treeNodeLevel.Node.Left, next_level))
        stack = append(stack, CreateTreeNodeLevel(treeNodeLevel.Node.Right, next_level))
    }
    return bottomLeftValue
}
