class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = 0
        border_y = m - 1
        border_x = n - 1

        def helper(y, x):
            nonlocal paths
            if y == border_y and x == border_x:
                paths += 1
                return
            if y < border_y:
                helper(y + 1, x)
            if x < border_x:
                helper(y, x + 1)

        helper(0, 0)
        return paths


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n] * m
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    grid[i][j] = 1
                    continue
                if i == 0:
                    grid[i][j] = grid[i][j - 1]
                    continue
                if j == 0:
                    grid[i][j] = grid[i - 1][j]
                    continue
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        return grid[m - 1][n - 1]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        return grid[m - 1][n - 1]


m = 3
n = 7

s = Solution()
print(s.uniquePaths(m, n))
