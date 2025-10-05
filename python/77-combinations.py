class Solution:
    def __init__(self):
        self.results = []
        self.visited = set()

    def helper(self, n, k, path=""):
        if len(path) == k:
            standardized = sorted(list(path))
            standardized[:] = map(lambda x: int(x), standardized)
            self.results.append(standardized)
            return
        for i in range(n + 1):
            if str(i + 1) in path:
                return
            self.helper(n, k, path + str(i + 1))

    def combine(self, n: int, k: int) -> list[list[int]]:
        for i in range(n):
            self.helper(n, k, path=str(i + 1))
        return sorted(self.results)


s = Solution()
print(s.combine(4, 2))
