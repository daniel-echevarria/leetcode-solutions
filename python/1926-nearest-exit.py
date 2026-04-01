from collections import deque


class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        m = len(maze)
        n = len(maze[0])

        visited = set()
        queue = deque([(entrance, 0)])

        while queue:
            position, steps = deque.popleft(queue)
            [x, y] = position
            if (x, y) in visited or maze[x][y] == "+":
                continue
            visited.add((x, y))
            if (x - 1 < 0 or x + 1 > m - 1 or y - 1 < 0 or y + 1 > n - 1) and [
                x,
                y,
            ] != entrance:
                return steps

            if x - 1 >= 0:
                queue.append(([x - 1, y], steps + 1))
            # move right
            if y + 1 <= n - 1:
                queue.append(([x, y + 1], steps + 1))
            # move down
            if x + 1 <= m - 1:
                queue.append(([x + 1, y], steps + 1))
            # move left
            if y - 1 >= 0:
                queue.append(([x, y - 1], steps + 1))
        return -1


maze = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]]
entrance = [1, 2]
# maze = [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]]
# entrance = [1, 0]

s = Solution()
print(s.nearestExit(maze, entrance))
