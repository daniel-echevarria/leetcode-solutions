class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        children = 0

        for size in s:
            if children == len(g):
                break

            if size >= g[children]:
                children += 1

        return children
