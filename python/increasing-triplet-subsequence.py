class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        base = [nums[0]]
        alt = []
        for i in range(1, n):
            num = nums[i]
            if base[-1] < num:
                base.append(num)
            elif len(base) == 1:
                base[-1] = num
            elif len(base) == 2:
                if base[-2] < num:
                    base[-1] = num
                else:
                    if not alt or alt[-1] < num:
                        alt.append(num)
                    else:
                        alt[-1] = num
            if len(base) == len(alt):
                while base and alt[0] < base[-1]:
                    base.pop()
                base += alt
                alt = []
            #print(base)
            #print(alt)
            #print("------")
            if len(base) == 3:
                return True
        return False
