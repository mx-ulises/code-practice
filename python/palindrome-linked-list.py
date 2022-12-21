# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def get_node_count(node: Optional[ListNode]) -> int:
        n = 0
        while node:
            node = node.next
            n += 1
        return n

    def get_mid_node(node: Optional[ListNode], n: int) -> Optional[ListNode]:
        for _ in range(n // 2):
            node = node.next
        return node

    def revert(node: Optional[ListNode]) -> Optional[ListNode]:
        if node == None:
           return None
        prev = None
        while node.next != None:
            aux = node
            node = node.next
            aux.next = prev
            prev = aux
        node.next = prev
        return node

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        n = Solution.get_node_count(head)
        mid_node = Solution.get_mid_node(head, n)
        reverted_half = Solution.revert(mid_node)
        for _ in range(n // 2):
            if reverted_half.val != head.val:
                return False
            reverted_half = reverted_half.next
            head = head.next
        return True
