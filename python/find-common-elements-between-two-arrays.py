class Solution:
    def add_map(nums: List[int], intersection_map: Dict[int, int], mask: int):
        for num in nums:
            intersection_map[num] |= mask

    def count_elements(intersection_map: Dict[int, int], nums: List[int]):
        elements = 0
        for num in nums:
            if intersection_map[num] == 3:
                elements += 1
        return elements

    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection_map = defaultdict(lambda: 0)
        Solution.add_map(nums1, intersection_map, 1)
        Solution.add_map(nums2, intersection_map, 2)
        return [
            Solution.count_elements(intersection_map, nums1),
            Solution.count_elements(intersection_map, nums2)
        ]
