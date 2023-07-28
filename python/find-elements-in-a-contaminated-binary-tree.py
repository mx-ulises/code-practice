# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        s = [(root, 0)]
        while s:
            node, value = s.pop()
            if node == None:
                continue
            node.val = value
            s.append((node.left, (2 * value) + 1))
            s.append((node.right, (2 * value) + 2))

    def _get_route(target: int) -> List[int]:
        route = []
        while target != 0:
            parent = (target - 1) // 2
            if target - (parent * 2) == 2:
                route.append(1)
            else:
                route.append(0)
            target = parent
        return route

    def find(self, target: int) -> bool:
        route = FindElements._get_route(target)
        current = self.root
        while route and current != None:
            direction = route.pop()
            if direction == 0:
                current = current.left
            else:
                current = current.right
        return current != None

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
