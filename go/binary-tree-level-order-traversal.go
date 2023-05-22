/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

 type TreeNodeLevel struct {
    Node *TreeNode
    Level int
}

func levelOrder(root *TreeNode) [][]int {
    s := []TreeNodeLevel{}
    s = append(s, TreeNodeLevel{Node: root, Level: 0})
    LevelOrder := [][]int{}
    for 0 < len(s) {
        treeNodeLevel := s[0]
        s = s[1:]
        node := treeNodeLevel.Node
        level := treeNodeLevel.Level
        if node == nil {
            continue
        }
        if level == len(LevelOrder) {
            LevelOrder = append(LevelOrder, []int{})
        }
        LevelOrder[level] = append(LevelOrder[level], node.Val)
        s = append(s, TreeNodeLevel{Node: node.Left, Level: level + 1})
        s = append(s, TreeNodeLevel{Node: node.Right, Level: level + 1})
    }
    return LevelOrder
}
