# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        prev = None
        current = head
        while current != None and current.next != None:
            current_next = current.next
            jump = current_next.next
            current.next = jump
            current_next.next = current
            if prev == None:
                head = current_next
            else:
                prev.next = current_next
            prev = current
            current = jump
        return head
