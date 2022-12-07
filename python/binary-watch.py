LED_VALUES = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

class Solution:

    def get_combinations(turnedOn: int, current_index: int, current_sum: int, combinations: List[str]):
        if turnedOn == 0:
            hours = current_sum // 64
            seconds = current_sum % 64
            if hours < 12 and seconds < 60:
                combinations.append("{}:{}".format(str(hours), str(seconds).zfill(2)))
        else:
            for index in range(current_index, len(LED_VALUES)):
                current_sum += LED_VALUES[index]
                Solution.get_combinations(turnedOn - 1, index + 1, current_sum, combinations)
                current_sum -= LED_VALUES[index]


    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        combinations = []
        Solution.get_combinations(turnedOn, 0, 0, combinations)
        return combinations
