class Solution:
    def with_pop(batteryPercentages: List[int]) -> int:
        device_test_count = 0
        offset = 0
        while batteryPercentages:
            percentage = max(batteryPercentages.pop(0) - offset, 0)
            if 0 < percentage:
                device_test_count += 1
                offset += 1
        return device_test_count

    def with_ineration(batteryPercentages: List[int]) -> int:
        device_test_count = 0
        offset = 0
        for original_percentage in batteryPercentages:
            percentage = max(original_percentage - offset, 0)
            if 0 < percentage:
                device_test_count += 1
                offset += 1
        return device_test_count

    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        return Solution.with_ineration(batteryPercentages)
