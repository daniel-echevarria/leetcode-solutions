class Solution:
    def reverseBits(self, n: int) -> int:
        start = 0
        for _ in range(32):
            bit = n & 1
            start = (start << 1) | bit
            n >>= 1
        return start


s = Solution()
n = 43261596
s.reverseBits(n)
