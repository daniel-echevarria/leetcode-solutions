from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        queue = deque()
        ones = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append([i, j])
                elif grid[i][j] == 1:
                    ones += 1
        minutes = 0
        if not ones:
            return 0
        if not queue:
            return -1
        while queue:
            for i in range(len(queue)):
                [x, y] = queue.popleft()
                if x - 1 >= 0 and grid[x - 1][y] == 1:
                    queue.append([x - 1, y])
                    grid[x - 1][y] = 2
                if x + 1 <= m - 1 and grid[x + 1][y] == 1:
                    queue.append([x + 1, y])
                    grid[x + 1][y] = 2
                if y - 1 >= 0 and grid[x][y - 1] == 1:
                    queue.append([x, y - 1])
                    grid[x][y - 1] = 2
                if y + 1 <= n - 1 and grid[x][y + 1] == 1:
                    queue.append([x, y + 1])
                    grid[x][y + 1] = 2
            minutes += 1
        if any(x == 1 for row in grid for x in row):
            return -1
        return minutes - 1


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        queue = deque()
        ones = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append([i, j])
                elif grid[i][j] == 1:
                    ones += 1

        if not ones:
            return 0
        if not queue:
            return -1

        minutes = 0
        while queue and ones > 0:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        ones -= 1
                        queue.append((nx, ny))
            minutes += 1

        return minutes if ones == 0 else -1


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]

s = Solution()
print(s.orangesRotting(grid))

# Algo, make a queue of all the rotten nodes
# move them to visited
# that's minute 0
# add all the neighbors to the queue
# add one minute
# after all that if there are no more fresh oranges return the number of minutes
# otherwise return -1
