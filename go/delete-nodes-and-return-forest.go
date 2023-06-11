/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

 func CreateForest(node *TreeNode, toDelete map[int]bool, forest *[]*TreeNode) bool{
    if node == nil {
        return false
    }
    if CreateForest(node.Left, toDelete, forest) {
        node.Left = nil
    }
    if CreateForest(node.Right, toDelete, forest) {
        node.Right = nil
    }
    if toDelete[node.Val] == true {
        if node.Left != nil {
            *(forest) = append(*(forest), node.Left)
        }
        if node.Right != nil {
            *(forest) = append(*(forest), node.Right)
        }
        return true
    }
    return false
}

func delNodes(root *TreeNode, to_delete []int) []*TreeNode {
    forest := make([]*TreeNode, 0)
    toDelete := make(map[int]bool)
    for i := 0; i < len(to_delete); i++ {
        toDelete[to_delete[i]] = true
    }
    deleteRoot := CreateForest(root, toDelete, &forest)
    if deleteRoot == false {
        forest = append(forest, root)
    }
    //fmt.Println(forest)
    return forest
}
