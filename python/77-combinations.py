class Solution:
    def __init__(self):
        self.results = []

    def helper(self, n, k, path=[], current=0):
        if len(path) == k:
            self.results.append(path)
            return
        for i in range(current, n):
            self.helper(n, k, [*path, i + 1], i + 1)

    def combine(self, n: int, k: int) -> list[list[int]]:
        self.helper(n, k)
        return self.results


s = Solution()
print(s.combine(4, 2))
