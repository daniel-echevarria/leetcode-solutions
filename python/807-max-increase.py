class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        n = len(grid)
        col_grid = []
        total_height = 0

        for i in range(n):
            col = []
            for j in range(n):
                col.append(grid[j][i])
            col_grid.append(col)

        for i in range(n):
            for j in range(n):
                new_height = min(max(grid[i]), max(col_grid[j]))
                previous_height = grid[i][j]
                total_height += new_height - previous_height
        return total_height


grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
s = Solution()
print(s.maxIncreaseKeepingSkyline(grid))
