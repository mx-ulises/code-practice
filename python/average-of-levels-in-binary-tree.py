# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        elements = []
        s = [(root, 0)]
        while s:
            node, level = s.pop()
            if node == None:
                continue
            if len(elements) == level:
                elements.append([node.val, 1])
            else:
                elements[level][0] += node.val
                elements[level][1] += 1
            s.append((node.left, level + 1))
            s.append((node.right, level + 1))
        averages = [summatory/n for summatory, n in elements]
        return averages
