class Solution:
    def countBits(self, n: int) -> list[int]:
        res = []
        for i in range(n + 1):
            num_ones = bin(i).count("1")
            res.append(num_ones)
        return res


class Solution:
    def countBits(self, n: int) -> list[int]:
        threshold = 0
        running = 0

        res = []
        for _ in range(n + 1):
            res.append(running)
            if running == threshold:
                threshold += 1
                running = 1
                continue
            running += 1
        return res


s = Solution()
print(s.countBits(6))
