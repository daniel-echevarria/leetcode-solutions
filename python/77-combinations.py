class Solution:
    def __init__(self):
        self.results = []
        self.visited = set()

    def helper(self, n, k, path=""):
        if len(path) == k:
            standardized = list(path).sort()
            self.results.append(standardized)
            return

    def combine(self, n: int, k: int) -> list[list[int]]:
        for i in range(n):
            self.helper(n, k, path=str(i + 1))
