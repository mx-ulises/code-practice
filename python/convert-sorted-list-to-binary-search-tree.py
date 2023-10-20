# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insert_into_bst(node: Optional[TreeNode], val) -> Optional[TreeNode]:
        if node == None:
            return TreeNode(val=val)
        elif val < node.val:
            node.left = Solution.insert_into_bst(node.left, val)
        else:
            node.right = Solution.insert_into_bst(node.right, val)
        return node

    def linked_list_to_array(head: Optional[ListNode]) -> List[int]:
        vals = []
        cur = head
        while cur:
            vals.append(cur.val)
            cur = cur.next
        return vals

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        vals = Solution.linked_list_to_array(head)
        s = [(0, len(vals) - 1)]
        root = None
        while s:
            start, end = s.pop()
            if end < start:
                continue
            mid = (start + end) // 2
            root = Solution.insert_into_bst(root, vals[mid])
            s.append((start, mid - 1))
            s.append((mid + 1, end))
        return root
