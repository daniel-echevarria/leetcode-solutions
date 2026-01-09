class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        delta = [0] * 52

        for start, end in ranges:
            delta[start] += 1
            delta[end + 1] -= 1

        active_ranges = 0

        for i in range(51):
            active_ranges += delta[i]
            if left <= i <= right and active_ranges < 1:
                return False
        return True


s = Solution()
ranges = [[1, 2], [3, 4], [5, 6]]
left = 2
right = 5
print(s.isCovered(ranges, left, right))

# Algo
# declare an an array delta of length 50 with initial values of 0
# iterate through the ranges
# add 1 for each start  and decrement 1 for each end
# return wether both left and right are bigger than 0
