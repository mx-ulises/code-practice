class Solution:
    def add_array_to_heap(nums1: List[int], nums2: List[int]) -> List[List[int]]:
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

    def use_heap_and_set(nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h = [(nums1[0] + nums2[0], 0, 0)]
        pairs = set()
        while len(pairs) < k and h:
            _, u, v = heappop(h)
            if (u, v) in pairs:
                continue
            pairs.add((u, v))
            u_next = u + 1
            if u_next < len(nums1):
                heappush(h, ((nums1[u_next] + nums2[v]), u_next, v))
            v_next = v + 1
            if v_next < len(nums2):
                heappush(h, ((nums1[u] + nums2[v_next]), u, v_next))
        return [(nums1[u], nums2[v]) for u, v in pairs]

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        return Solution.use_heap_and_set(nums1, nums2, k)
