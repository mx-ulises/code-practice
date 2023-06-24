# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, head: ListNode, a: int, b: int, segment_2_head: ListNode) -> ListNode:
        segment_2_tail = segment_2_head
        while segment_2_tail.next != None:
            segment_2_tail = segment_2_tail.next
        removed_segment_tail = head
        segment_1_tail = head
        for i in range(b):
            if a - i == 1:
                segment_1_tail = removed_segment_tail
            removed_segment_tail = removed_segment_tail.next
        segment_1_tail.next = segment_2_head
        segment_2_tail.next = removed_segment_tail.next
        return head
