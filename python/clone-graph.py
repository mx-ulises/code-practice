"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        root = node
        nodes = {}
        s = [root]
        while s:
            node = s.pop()
            if node and node not in nodes:
                nodes[node] = Node(node.val)
                for neighbor in node.neighbors:
                    s.append(neighbor)
        for node in nodes:
            new_node = nodes[node]
            for neighbor in node.neighbors:
                new_node.neighbors.append(nodes[neighbor])
        return nodes[root]
