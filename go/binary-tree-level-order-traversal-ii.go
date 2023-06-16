/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type PairTreeNodeLevel struct {
	Node  *TreeNode
	Level int
}

func reverseList(list [][]int) [][]int {
	length := len(list)
	for i := 0; i < (length / 2); i++ {
		list[i], list[length-i-1] = list[length-i-1], list[i]
	}
	return list
}

func levelOrderBottom(root *TreeNode) [][]int {
	levels := make([][]int, 0)
	s := make([]PairTreeNodeLevel, 0)
	s = append(s, PairTreeNodeLevel{Node: root, Level: 0})
	for 0 < len(s) {
		pair := s[0]
		s = s[1:]
		if pair.Node == nil {
			continue
		}
		if pair.Level == len(levels) {
			levels = append(levels, make([]int, 0))
		}
		levels[pair.Level] = append(levels[pair.Level], pair.Node.Val)
		s = append(s, PairTreeNodeLevel{Node: pair.Node.Left, Level: pair.Level + 1})
		s = append(s, PairTreeNodeLevel{Node: pair.Node.Right, Level: pair.Level + 1})
	}
	levels = reverseList(levels)
	return levels
}
