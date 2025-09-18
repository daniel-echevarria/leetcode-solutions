from collections import deque


class Solution:
    def numToCoordinates(self, num: int, board_size: int):
        row_from_bottom = (num - 1) // board_size
        row = board_size - 1 - row_from_bottom
        col = (num - 1) % board_size
        if row_from_bottom % 2 != 0:
            col = board_size - 1 - col
        return (row, col)

    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        goal = n * n
        visited = [False] * goal
        queue = deque([1])
        rolls = 0
        while queue:
            rolls += 1
            for _ in range(len(queue)):
                current = queue.popleft()
                for i in range(1, 7):
                    nxt = current + i
                    if nxt > goal:
                        continue
                    row, col = self.numToCoordinates(nxt, n)
                    dest = nxt if board[row][col] == -1 else board[row][col]
                    if dest == goal:
                        return rolls
                    if visited[dest - 1]:
                        continue

                    queue.append(dest)
                    visited[dest - 1] = True
        return -1


s = Solution()
print(
    s.snakesAndLadders(
        [
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 35, -1, -1, 13, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 15, -1, -1, -1, -1],
        ]
    )
)


# Iterate through the board and change the values to the numbers
