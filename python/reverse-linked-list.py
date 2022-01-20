class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = [None]
        current = head
        while current:
            s.append(current)
            current = current.next
        head = s.pop()
        current = head
        while current:
            current.next = s.pop()
            current = current.next
        return head
