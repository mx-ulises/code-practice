"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []
        s = [root]
        l = []
        while s:
            node = s.pop()
            l.append(node.val)
            for child in node.children:
                s.append(child)
        l.reverse()
        return l
