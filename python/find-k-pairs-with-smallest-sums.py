class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h = []
        pairs = []
        for i in range(len(nums1)):
            h.append((nums1[i] + nums2[0], i, 0))
        while len(pairs) < k and h:
            _, u, v = heappop(h)
            pairs.append((nums1[u], nums2[v]))
            v_next = v + 1
            if v_next < len(nums2):
                total = (nums1[u] + nums2[v_next])
                heappush(h, (total, u, v_next))
        return pairs
