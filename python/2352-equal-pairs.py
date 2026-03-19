from collections import defaultdict


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        cols = defaultdict(int)
        for j in range(n):
            col = []
            for i in range(n):
                col.append(grid[i][j])
            cols[tuple(col)] += 1
        pair_count = 0
        for row in grid:
            if tuple(row) in cols:
                pair_count += cols[tuple(row)]
        return pair_count


# grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
grid = [[3, 1, 2, 2], [1, 4, 4, 4], [2, 4, 2, 2], [2, 5, 2, 2]]
s = Solution()
print(s.equalPairs(grid))


# Algo
# Get columns
# make a set of rows and columns
# iterate through the rows and match with columns
