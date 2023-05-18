class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_altitude = 0
        maximal_altitude = 0
        for g in gain:
            current_altitude += g
            maximal_altitude = max(maximal_altitude, current_altitude)
        return maximal_altitude
