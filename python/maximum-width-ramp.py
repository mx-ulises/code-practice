class Solution:
    '''
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        left_candidates = [0]
        right_candidates = [n - 1]
        for i in range(1, n):
            if nums[i] < nums[left_candidates[-1]]:
                left_candidates.append(i)
            j = n - i - 1
            if nums[right_candidates[-1]] < nums[j]:
                right_candidates.append(j)
        right_nums = [nums[i] for i in right_candidates]
        ramp = 0
        for i in left_candidates:
            x = nums[i]
            indx = bisect_left(right_nums, x)
            if indx < len(right_nums):
                j = right_candidates[indx]
                ramp = max(ramp, j - i)
        return ramp
    '''


    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        left_candidates = [(nums[0], 0)]
        right_candidates = [(nums[n - 1], n - 1)]
        for i in range(1, n):
            if nums[i] < left_candidates[-1][0]:
                left_candidates.append((nums[i], i))
            j = n - i - 1
            if right_candidates[-1][0] < nums[j]:
                right_candidates.append((nums[j], j))
        ramp = 0
        while left_candidates and right_candidates:
            #print(left_candidates)
            #print(right_candidates)
            if left_candidates[0][0] <= right_candidates[-1][0]:
                new_ramp = right_candidates[-1][1] - left_candidates[0][1]
                ramp = max(ramp, new_ramp)
                #print(ramp)
                right_candidates.pop()
            else:
                left_candidates.pop(0)
            #print("-----------")
        return ramp
