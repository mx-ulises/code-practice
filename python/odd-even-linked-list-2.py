# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        odd_head = head
        odd_tail = odd_head
        #print(odd_tail.val)
        even_head = head.next
        even_tail = even_head
        current = None
        if head.next:
            #print(even_tail.val)
            current = head.next.next
        while current:
            odd_tail.next = current
            odd_tail = odd_tail.next
            current = current.next
            #print(odd_tail.val)
            if current:
                even_tail.next = current
                even_tail = even_tail.next
                current = current.next
                #print(even_tail.val)
        odd_tail.next = even_head
        if even_tail:
            even_tail.next = None
        current = odd_head
        return odd_head
