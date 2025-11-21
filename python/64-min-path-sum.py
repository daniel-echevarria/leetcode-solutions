class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]


s = Solution()
grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(s.minPathSum(grid))

# Iterate through rows and cols using this formula
# The current value gets the minimum of the upper or left value if they exist
# return the last value
