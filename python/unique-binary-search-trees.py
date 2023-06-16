class Solution:
    def numTrees(self, n: int) -> int:
        trees = [1, 1]
        for total_nodes in range(2, n + 1):
            trees.append(0)
            for left_nodes in range(0, total_nodes):
                right_nodes = total_nodes - left_nodes - 1
                trees[total_nodes] += trees[left_nodes] * trees[right_nodes]
        return trees[n]
