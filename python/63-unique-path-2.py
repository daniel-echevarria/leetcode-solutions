class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                elif i == 0 and j == 0:
                    obstacleGrid[i][j] = 1
                elif i == 0:
                    obstacleGrid[i][j] += obstacleGrid[i][j - 1]
                elif j == 0:
                    obstacleGrid[i][j] += obstacleGrid[i - 1][j]
                else:
                    obstacleGrid[i][j] += (
                        obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
                    )
        return obstacleGrid[-1][-1]


s = Solution()
obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(s.uniquePathsWithObstacles(obstacleGrid))


# Algo, for each square if the square is 1, continue otherwise it becomes the sum
# of the top and left square if they exist
