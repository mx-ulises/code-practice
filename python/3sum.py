class Solution:
    def binary_search(nums, target, start, end) -> bool:
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        prev_i = -10001
        n = len(nums)
        for i in range(n - 2):
            a = nums[i]
            if a == prev_i:
                continue
            prev_j = -10001
            for j in range(i + 1, n - 1):
                b = nums[j]
                if b == prev_j:
                    continue
                c = -(a + b)
                if Solution.binary_search(nums, c, j + 1, n - 1):
                    output.append([a, b, c])
                prev_j = b
            prev_i = a
        return output
