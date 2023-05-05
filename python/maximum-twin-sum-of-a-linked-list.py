# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prev = None
        runner = head
        current = head
        while runner:
            runner = runner.next.next
            aux = current.next
            current.next = prev
            prev = current
            current = aux
        maximal = 0
        while current:
            maximal = max(maximal, prev.val + current.val)
            prev = prev.next
            current = current.next
        return maximal
