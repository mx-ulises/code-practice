RANGE_TEMPLATE = "{0}->{1}"

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        summary = []
        start_range = nums[0]
        end_range = nums[0]
        for i in range(1, len(nums)):
            if (end_range + 1) != nums[i]:
                if start_range == end_range:
                    summary.append(str(start_range))
                else:
                    summary.append(RANGE_TEMPLATE.format(start_range, end_range))
                start_range = nums[i]
            end_range = nums[i]
        if start_range == end_range:
            summary.append(str(start_range))
        else:
            summary.append(RANGE_TEMPLATE.format(start_range, end_range))
        return summary
