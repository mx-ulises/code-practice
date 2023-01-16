class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        nums3_set = set(nums3)
        nums4_set = {x for x in nums1_set if x in nums2_set or x in nums3_set}
        for x in nums2_set:
            if x in nums3_set:
                nums4_set.add(x)
        return list(nums4_set)
