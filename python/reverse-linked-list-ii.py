# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        current = head
        prev = None
        l1_tail,  l2_head, l2_tail, l3_head = None, None, None, None
        while current:
            left -= 1
            right -= 1
            if left == 1:
                l1_tail = current
            if left == 0:
                l2_tail = current
            if right == 0:
                l2_head = current
            if right == -1:
                l3_head = current
            succ = current.next
            if left < 0 and 0 <= right:
                current.next = prev
            prev = current
            current = succ
        if not l1_tail:
            head = l2_head
        else:
            l1_tail.next = l2_head
        l2_tail.next = l3_head
        return head
