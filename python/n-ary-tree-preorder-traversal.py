"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

def get_preorder(node, output):
    if node == None:
        return
    output.append(node.val)
    for child in node.children:
        get_preorder(child, output)

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        output = []
        get_preorder(root, output)
        return output
