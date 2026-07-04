class Solution:
    def minFlips(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        columns = [["#"] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                columns[j][i] = grid[i][j]

        row_swaps = col_swaps = 0
        for row in grid:
            l, r = 0, n - 1
            while l < r:
                if row[l] != row[r]:
                    row_swaps += 1
                l += 1
                r -= 1
        for cols in columns:
            l, r = 0, m - 1
            while l < r:
                if cols[l] != cols[r]:
                    col_swaps += 1
                l += 1
                r -= 1
        return min(row_swaps, col_swaps)


# grid = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
grid = [[0, 1], [0, 1], [0, 0]]
s = Solution()
print(s.minFlips(grid))
