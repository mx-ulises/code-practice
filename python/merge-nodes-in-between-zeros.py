# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head.next
        valid_node = head
        while current:
            if current.val == 0:
                valid_node.next = current
                prev = valid_node
                valid_node = current
            valid_node.val += current.val
            current = current.next
        prev.next = None
        return head
