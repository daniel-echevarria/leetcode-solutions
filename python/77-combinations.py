class Solution:
    def __init__(self):
        self.results = []

    def helper(self, n, k, path):
        if len(path) == k:
            self.results.append(path)
            return
        for i in range(n + 1):
            if i + 1 in path:
                return
            self.helper(n, k, [*path, i + 1])

    def combine(self, n: int, k: int) -> list[list[int]]:
        for i in range(n):
            self.helper(n, k, path=[i + 1])
        return self.results
