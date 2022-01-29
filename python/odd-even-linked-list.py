'''
Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Empty lsit scenario
        if head == None:
            return None

        # Initializing heads and current pointers
        odd_current = head
        even_head = head.next
        even_current = even_head

        # pick first node to analyze
        current = even_current
        is_odd = True

        # Check until we arrive to the end of the list
        while current != None:
            current = current.next
            if is_odd and current: #only if node is not Null
                is_odd = False
                odd_current.next = current
                odd_current = odd_current.next
            else:
                is_odd = True
                even_current.next = current
                even_current = even_current.next

        odd_current.next = even_head
        return head
