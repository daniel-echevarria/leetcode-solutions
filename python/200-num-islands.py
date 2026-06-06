class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        islands = 0

        def dfs(row, col):
            if not (0 <= row < m and 0 <= col < n) or grid[row][col] == "0":
                return
            grid[row][col] = "0"
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1
        return islands


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]

s = Solution()
print(s.numIslands(grid))

# Algo for each cell in the grid, if it's a one, submerge all neighbors and add one to the counts
