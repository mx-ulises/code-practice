# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
        pred = None
        current = head
        while current:
            succ = current.next
            current.next = pred
            pred = current
            current = succ
        return pred

    def extend_if_none(current: Optional[ListNode], prev: Optional[ListNode]) -> Optional[ListNode]:
        if current == None:
                current = ListNode()
                prev.next = current
        return current

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = Solution.reverse(l1)
        l2 = Solution.reverse(l2)
        carry = 0
        prev_1, prev_2 = None, None
        current_1, current_2 = l1, l2
        while current_1 != None or current_2 != None or 0 < carry:
            current_1 = Solution.extend_if_none(current_1, prev_1)
            current_2 = Solution.extend_if_none(current_2, prev_2)
            current_1.val += current_2.val + carry
            carry = current_1.val // 10
            current_1.val %= 10
            prev_1, prev_2 =current_1, current_2
            current_1, current_2 = current_1.next, current_2.next
        return Solution.reverse(l1)
