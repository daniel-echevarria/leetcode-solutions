from collections import defaultdict
from collections import deque


class Solution:
    def sortMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        my_dict = defaultdict(list)
        for i in range(n):
            for j in range(n):
                my_dict[i - j].append(grid[i][j])

        for key in my_dict:
            if key < 0:
                my_dict[key] = deque(sorted(my_dict[key]))
            else:
                my_dict[key] = deque(sorted(my_dict[key], reverse=True))

        for i in range(n):
            for j in range(n):
                grid[i][j] = my_dict[i - j].popleft()
        return grid


grid = [[1, 7, 3], [9, 8, 2], [4, 5, 6]]
s = Solution()
print(s.sortMatrix(grid))
