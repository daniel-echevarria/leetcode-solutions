class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        grid = [""] * len(strs[0])
        for s in strs:
            for i in range(len(s)):
                grid[i] += s[i]

        count = 0
        for s in grid:
            if s != "".join(sorted(s)):
                count += 1
        return count


strs = ["cba", "daf", "ghi"]
s = Solution()
print(s.minDeletionSize(strs))


# Algo
# make the grid
# compare each string to the sorted version
# count deltetion
