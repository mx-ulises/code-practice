class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2_copy = list(nums2)
        nums2.sort()
        tail = []
        nums_map = defaultdict(list)
        i = 0
        while nums1:
            x = nums1.pop(0)
            y = nums2[i]
            if y < x:
                nums_map[y].append(x)
                i += 1
            else:
                tail.append(x)
        for x in tail:
            y = nums2[i]
            nums_map[y].append(x)
            i += 1
        return [nums_map[x].pop() for x in nums2_copy]
