class Solution:

    def numberOfBeams(self, bank: List[str]) -> int:
        num_of_beams = 0
        n = len(bank)
        i = 0
        current_floor_devices = 0
        while i < n and current_floor_devices == 0:
            current_floor_devices = sum(map(int, bank[i]))
            i += 1
        j = i
        while j < n:
            next_floor_devices = 0
            while j < n and next_floor_devices == 0:
                next_floor_devices = sum(map(int, bank[j]))
                j += 1
            if 0 < next_floor_devices:
                num_of_beams += current_floor_devices * next_floor_devices
            current_floor_devices = next_floor_devices
        return num_of_beams


    def numberOfBeams_better(self, bank: List[str]) -> int:
        num_of_beams = 0
        zeros = "0" * len(bank[0])
        devices_per_floor = [floor.count("1") for floor in bank if floor != zeros]
        for i in range(len(devices_per_floor) - 1):
            num_of_beams += devices_per_floor[i] * devices_per_floor[i + 1]
        return num_of_beams
