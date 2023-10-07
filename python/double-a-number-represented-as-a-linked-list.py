# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def stack_solution(head: Optional[ListNode]) -> Optional[ListNode]:
        # Add elements to a stack so we can access them in reverse order
        s = []
        current = head
        while current:
            s.append(current)
            current = current.next
        carry = 0
        # Double the elements from least to most significant, and add the carry
        while s:
            current = s.pop()
            value = current.val * 2 + carry
            carry = value // 10
            current.val = value % 10
        # If we have carry, create a new head with this value
        if 0 < carry:
            head = ListNode(val=carry, next=head)
        return head

    def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            succesor = current.next
            current.next = prev
            prev = current
            current = succesor
        return prev

    def reverse_solution(head: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse list to get from least to most significant
        head = Solution.reverse(head)
        # Double items from least to most significant with carry
        current = head
        carry = 0
        prev = None
        while current:
            current.val = current.val * 2 + carry
            carry = current.val // 10
            current.val = current.val % 10
            prev = current
            current = current.next
        # Create a tail element if carry exists
        if 0 < carry:
            prev.next = ListNode(val=carry)
        # Return reversed list form most to least significant
        return Solution.reverse(head)

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return Solution.reverse_solution(head)
