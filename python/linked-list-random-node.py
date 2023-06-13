# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.nodes = []
        current = head
        while current:
            self.nodes.append(current.val)
            current = current.next

    def getRandom(self) -> int:
        val = self.nodes[randint(0, len(self.nodes) - 1)]
        return val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
