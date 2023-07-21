# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def get_nodes(root: TreeNode):
        nodes = []
        s = [root]
        while s:
            node = s.pop()
            if node == None:
                continue
            nodes.append((node.val, node))
            s.append(node.left)
            s.append(node.right)
            node.left = None
            node.right = None
        return nodes

    def build_bbst(nodes, start_index, end_index) -> TreeNode:
        if end_index < start_index:
            return None
        mid_index = (end_index - start_index) // 2 + start_index
        node = nodes[mid_index][1]
        #print(f"node: {node.val}, start: {start_index}, end: {end_index}, mid: {mid_index}")
        node.left = Solution.build_bbst(nodes, start_index, mid_index - 1)
        node.right = Solution.build_bbst(nodes, mid_index + 1, end_index)
        return node

    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = Solution.get_nodes(root)
        nodes.sort()
        root = Solution.build_bbst(nodes, 0, len(nodes) - 1)
        return root
