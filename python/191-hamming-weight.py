class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += 1
            n &= n - 1
        return count


s = Solution()
n = 11
print(s.hammingWeight(n))
