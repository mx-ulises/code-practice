class Solution:
    def pop_maximal(nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) == 0:
            return nums2.pop()
        elif len(nums2) == 0:
            return nums1.pop()
        elif nums1[-1] < nums2[-1]:
            return nums2.pop()
        else:
           return nums1.pop()

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        limit = total // 2 - 1 + (total & 1)
        for _ in range(limit):
            Solution.pop_maximal(nums1, nums2)
        if total & 1 == 0:
            a = Solution.pop_maximal(nums1, nums2)
            b = Solution.pop_maximal(nums1, nums2)
            return (a + b) / 2
        return Solution.pop_maximal(nums1, nums2)
