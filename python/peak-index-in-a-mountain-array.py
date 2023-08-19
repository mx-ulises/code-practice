class Solution:
    def get_peak_direction(arr: List[int], i: int) -> int:
        direction = 0
        if i == 0 or arr[i - 1] < arr[i]:
            direction += 1
        if i == len(arr) - 1 or arr[i] > arr[i + 1]:
            direction -= 1
        return direction

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        mid = (left + right) // 2
        direction = Solution.get_peak_direction(arr, mid)
        while direction != 0:
            if direction < 0:
                right = mid - 1
            else:
                left = mid + 1
            mid = (left + right) // 2
            direction = Solution.get_peak_direction(arr, mid)
        return mid
