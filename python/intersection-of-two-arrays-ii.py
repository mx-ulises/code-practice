class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums_1_dict = {}
        for x in nums1:
            nums_1_dict[x] = nums_1_dict.get(x, 0) + 1
        output = []
        for x in nums2:
            if nums_1_dict.get(x, 0):
                nums_1_dict[x] -= 1
                output.append(x)
        return output
