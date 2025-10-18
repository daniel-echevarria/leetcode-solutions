class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def same(self, grid):
        flat = [x for sub in grid for x in sub]
        if flat.count(0) == 0:
            return "one"
        if flat.count(1) == 0:
            return "zero"
        return False

    def construct(self, grid: list[list[int]]) -> "Node":
        n = len(grid)
        half = int(n / 2)
        samo = self.same(grid)
        if samo == "one":
            return Node(
                val=True,
                isLeaf=True,
                topLeft=None,
                topRight=None,
                bottomLeft=None,
                bottomRight=None,
            )
        if samo == "zero":
            return Node(
                val=False,
                isLeaf=True,
                topLeft=None,
                topRight=None,
                bottomLeft=None,
                bottomRight=None,
            )
        topLeft = [row[:half] for row in grid[:half]]
        topRight = [row[half:] for row in grid[:half]]
        bottomLeft = [row[:half] for row in grid[half:]]
        bottomRight = [row[half:] for row in grid[half:]]
        return Node(
            val=True,
            isLeaf=False,
            topLeft=self.construct(topLeft),
            topRight=self.construct(topRight),
            bottomLeft=self.construct(bottomLeft),
            bottomRight=self.construct(bottomRight),
        )
