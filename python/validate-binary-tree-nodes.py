NEW = 0
VISITED = 1
COMPLETED = 2
COMPLETED_WITH_PARENT = 3

def is_valid_tree(node, leftChild, rightChild, node_status):
    if node == -1:
        return True
    if node_status[node] == VISITED or node_status[node] == COMPLETED_WITH_PARENT:
        return False
    if node_status[node] == COMPLETED:
        node_status[node] = COMPLETED_WITH_PARENT
        return True
    node_status[node] = VISITED
    if not is_valid_tree(leftChild[node], leftChild, rightChild, node_status):
        return False
    if not is_valid_tree(rightChild[node], leftChild, rightChild, node_status):
        return False
    node_status[node] = COMPLETED
    return True


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        node_status = defaultdict(lambda: NEW)
        node_status[-1] = COMPLETED_WITH_PARENT
        for node in range(n):
            if not is_valid_tree(node, leftChild, rightChild, node_status):
                return False
        return n == len([1 for node in node_status if node_status[node] == COMPLETED_WITH_PARENT])
