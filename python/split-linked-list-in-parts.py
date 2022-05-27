# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        current = head
        n = 0
        while current:
            current = current.next
            n += 1
        current = head
        split_list = []
        while current:
            node_count = ceil(n / k)
            n -= node_count
            k -= 1
            split_list.append(current)
            node_count -= 1
            while current.next and node_count:
                node_count -= 1
                current = current.next
            current_next = current.next
            current.next = None
            current = current_next
        split_list.extend([None] * k)
        return split_list
