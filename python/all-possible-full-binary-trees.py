class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        memory = [[] for _ in range(n + 1)]
        memory[1].append(TreeNode(0))
        for node_count in range(3, n + 1, 2):
            for i in range(1, node_count - 1, 2):
                j = node_count - 1 - i
                for left in memory[i]:
                    for right in memory[j]:
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        memory[node_count].append(root)
        return memory[n]
