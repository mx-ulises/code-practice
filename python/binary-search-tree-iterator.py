# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:

    def _deep_insert(self, node: Optional[TreeNode]):
        while node:
            self.levels.append(node)
            node = node.left

    def __init__(self, root: Optional[TreeNode]):
        self.levels = []
        self._deep_insert(root)

    def next(self) -> int:
        if self.hasNext():
            node = self.levels.pop()
            self._deep_insert(node.right)
            return node.val
        return -1

    def hasNext(self) -> bool:
        return len(self.levels) != 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
