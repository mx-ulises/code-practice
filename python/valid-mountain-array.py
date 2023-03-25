class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        peak_achieved = False
        if len(arr) < 3:
            return False
        for i in range(1, len(arr)):
            if arr[i - 1] == arr[i]:
                return False
            elif arr[i - 1] < arr[i] and peak_achieved:
                return False
            elif arr[i] < arr[i - 1]:
                if i == 1:
                    return False
                peak_achieved = True
        return peak_achieved
