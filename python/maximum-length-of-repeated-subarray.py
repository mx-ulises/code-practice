class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        maximal = 0
        for i in range(n + m):
            j = max(n - 1 - i, 0)
            k = max(i - n, 0)
            count = 0
            while j < n and k < m:
                if nums1[j] == nums2[k]:
                    count += 1
                    maximal = max(maximal, count)
                else:
                    count = 0
                j += 1
                k += 1
        return maximal
