class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        right = []
        mid = []
        for x in nums:
            if x < pivot:
                left.append(x)
            elif x == pivot:
                mid.append(x)
            else:
                right.append(x)
        return left + mid + right
