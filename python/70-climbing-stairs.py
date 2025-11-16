class Solution:
    def climbStairs(self, n: int) -> int:
        steps = {}
        steps[1] = 1
        steps[2] = 2
        for num in range(3, n + 1):
            steps[num] = steps[num - 1] + steps[num - 2]
        return steps[n]


s = Solution()
print(s.climbStairs(5))
