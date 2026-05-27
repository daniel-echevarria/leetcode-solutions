class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        stack = [(0, 0)]
        visited = set()
        length = 0

        while stack:
            for _ in stack:
                row, col = stack.pop()
                visited.add((row, col))
                if grid[row][col] == 0:
                    [
                        (row + 1, col),
                        (row - 1, col),
                        (row, col + 1),
                        (row, col - 1),
                        (row + 1, col + 1),
                        (row - 1, col - 1),
                    ]
            for row, col in next_round:
                if (
                    0 <= row < n
                    and 0 <= col < n
                    and grid[row][col] == 0
                    and (row, col) not in visited
                ):
                    stack.append((row, col))
            length += 1
        return length

        # push all valid neighbors to the stack


from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1

        if n == 1:
            return 1

        queue = deque([(0, 0, 1)])
        visited = set({0, 0})
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (-1, -1),
            (-1, 1),
            (1, 1),
            (1, -1),
        ]

        while queue:
            for _ in range(len(queue)):
                row, col, length = deque.popleft(queue)
                for r, c in directions:
                    new_row = row + r
                    new_col = col + c
                    if new_row == n - 1 and new_col == n - 1:
                        return length + 1
                    if (
                        0 <= new_row < n
                        and 0 <= new_col < n
                        and (new_row, new_col) not in visited
                        and grid[new_row][new_col] == 0
                    ):
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col, length + 1))
        return -1


# grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
grid = [[0, 0, 0], [1, 0, 0], [1, 1, 0]]
s = Solution()
print(s.shortestPathBinaryMatrix(grid))
