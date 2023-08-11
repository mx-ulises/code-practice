/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func GetCoinMoves(node *TreeNode, currentMoves int) (int, int) {
	if node == nil {
		return 0, currentMoves
	}
	leftBalance, currentMoves := GetCoinMoves(node.Left, currentMoves)
	rightBalance, currentMoves := GetCoinMoves(node.Right, currentMoves)
	balance := leftBalance + rightBalance + node.Val - 1
	if leftBalance < 0 {
		leftBalance = -leftBalance
	}
	if rightBalance < 0 {
		rightBalance = -rightBalance
	}
	currentMoves += leftBalance + rightBalance
	return balance, currentMoves
}

func distributeCoins(root *TreeNode) int {
	_, moves := GetCoinMoves(root, 0)
	return moves
}
