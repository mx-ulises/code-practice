# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_primes(limit: int)  -> List[int]:
        primes = []
        cribe = [True] * (limit + 1)
        for i in range(2, limit + 1):
            if not cribe[i]:
                continue
            primes.append(i)
            non_prime = i * 2
            while non_prime <= limit:
                cribe[non_prime] = False
                non_prime += i
        return primes

    def getGCD(prev: int, succ: int, primes: List[int]):
        gcd = 1
        limit = min(prev, succ)
        i = 0
        while i < len(primes) and (gcd * primes[i]) <= limit:
            candidate = gcd * primes[i]
            while (prev % candidate) == 0 and (succ % candidate) == 0:
                gcd = candidate
                candidate = gcd * primes[i]
            i += 1
        return gcd

    def get_pairs_limit(head: Optional[ListNode]) -> int:
        pairs_limit = 1
        current = head
        while current.next != None:
            current_pairs_limit = min(current.val, current.next.val)
            pairs_limit = max(pairs_limit, current_pairs_limit)
            current = current.next
        return pairs_limit

    def manual_solution(head: Optional[ListNode]) -> Optional[ListNode]:
        pairs_limit = Solution.get_pairs_limit(head)
        primes = Solution.get_primes(pairs_limit)
        current = head
        while current.next != None:
            gcd = Solution.getGCD(current.val, current.next.val, primes)
            gcd_node = ListNode(gcd)
            gcd_node.next = current.next
            current.next = gcd_node
            current = current.next.next
        return head

    def optimal_solution(head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current.next != None:
            gcd = math.gcd(current.val, current.next.val)
            gcd_node = ListNode(gcd)
            gcd_node.next = current.next
            current.next = gcd_node
            current = current.next.next
        return head

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return Solution.optimal_solution(head)
