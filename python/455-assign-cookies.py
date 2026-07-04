class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        greed = size = 0
        count = 0
        while greed < len(g) and size < len(s):
            if s[size] < g[greed]:
                size += 1
            else:
                count += 1
                size += 1
                greed += 1
        return count


# Sort arrays
# create two pointers that start at 0
# loop as long as the indexes are smaller than the respective sizes of the lists
# if the size is smaller than the grid, increment the size
# if it's bigger or equal, increment both
