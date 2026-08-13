class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        return "".join(sorted(s1)) in "".join(sorted(s2))


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        visited = set()

        def dfs(idx, curr):
            if idx in visited or idx < 0 or idx > len(s2) - 1:
                return
            if curr == len(s1):
                return True
            increment = 0
            if s1[curr] == s2[idx]:
                visited.add(idx)
                increment = 1
            return dfs(idx - 1, curr + increment) or dfs(idx + 1, curr + increment)

        return dfs(0, 0)


from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1)

        freq = Counter(s1)
        freq2 = Counter(s2[l:r])

        if freq == freq2:
            return True

        while r < len(s2):
            removed_letter = s2[l]
            l += 1
            r += 1
            added_letter = s2[r - 1]
            freq2[removed_letter] -= 1
            freq2[added_letter] += 1
            if freq2[removed_letter] == 0:
                del freq2[removed_letter]
            if freq2 == freq:
                return True


# s1 = "ab"
# s2 = "eidbaooo"
# s1 = "a"
# s2 = "ab"
s1 = "adc"
s2 = "dcda"

s = Solution()
print(s.checkInclusion(s1, s2))
