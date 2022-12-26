class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = []
        next_element = defaultdict(lambda: -1)
        for x in nums2:
            while s and s[-1] < x:
                next_element[s.pop()] = x
            s.append(x)
        return [next_element[x] for x in nums1]
