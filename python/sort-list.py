# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        h = []
        current = head
        while current:
            heappush(h, (current.val, len(h), current))
            current = current.next
        _, _, head = heappop(h)
        current = head
        while h:
            current.next = h[0][2]
            _, _, current = heappop(h)
        current.next = None
        return head
