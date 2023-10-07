# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = []
        current = head
        while current:
            s.append(current)
            current = current.next
        residual = 0
        while s:
            current = s.pop()
            value = current.val * 2 + residual
            residual = value // 10
            current.val = value % 10
        if 0 < residual:
            head = ListNode(val=residual, next=head)
        return head
