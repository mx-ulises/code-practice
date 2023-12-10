class Solution:
    def add_numbers(num_map: Dict[int,int], nums: List[int], mask: int) -> None:
        for num in nums:
            num_map[num] |= mask

    def findDifference_self(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num_map = defaultdict(lambda: 0)
        Solution.add_numbers(num_map, nums1, 1)
        Solution.add_numbers(num_map, nums2, 2)
        answer = [[], []]
        for num in num_map:
            if num_map[num] == 1:
                answer[0].append(num)
            elif num_map[num] == 2:
                answer[1].append(num)
        return answer

    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        intersection = nums1 & nums2
        return [list(nums1 - intersection), list(nums2 - intersection)]
