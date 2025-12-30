class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        current = 0
        max_altitude = 0
        for n in gain:
            current += n
            max_altitude = max(max_altitude, current)
        return max_altitude


# Algo
# Iterate through the gain array computing the current altitude
# keep track of the max altitude
# return the max altitude
