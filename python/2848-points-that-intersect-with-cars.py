class Solution:
    def numberOfPoints(self, nums: list[list[int]]) -> int:
        line = [0] * 102
        for start, end in nums:
            line[start] += 1
            line[end + 1] -= 1

        curr = 0
        total_points = 0
        for i in range(101):
            curr += line[i]
            if curr > 0:
                total_points += 1
        return total_points


nums = [[3, 6], [1, 5], [4, 7]]
s = Solution()
print(s.numberOfPoints(nums))
