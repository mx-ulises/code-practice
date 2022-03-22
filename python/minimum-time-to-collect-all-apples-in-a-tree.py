REQUIRED = 1
NON_REQUIRED = 0
VISITED = -1
NON_VISITED = -2

def traverse(tree, a, status, hasApple):
    if NON_VISITED != status[a]:
        return
    status[a] = VISITED
    required = False
    for b in tree[a]:
        traverse(tree, b, status, hasApple)
        if status[b] == REQUIRED:
            required = True
    status[a] = NON_REQUIRED
    if hasApple[a] or required:
        status[a] = REQUIRED
    return status[a]

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        if sum(hasApple) == 0:
            return 0
        tree = defaultdict(list)
        for edge in edges:
            a, b = edge
            tree[a].append(b)
            tree[b].append(a)
        status = [NON_VISITED] * n
        for a in range(n):
            traverse(tree, a, status, hasApple)
        return (sum(status) - 1) * 2
