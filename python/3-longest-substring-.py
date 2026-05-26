from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_length = l = r = 0
        counts = defaultdict(int)

        while r < n:
            counts[s[r]] += 1
            while counts[s[r]] > 1:
                counts[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l)
            r += 1

        return max_length


st = "abcabcbb"
s = Solution()
print(s.lengthOfLongestSubstring(st))


# make a dict with counts per letters
# use two pointers left and right they both start at 0
# loop while the right pointer is smaller than the length of s
# the moment there is a duplication (the counts are bigger than 1)
# potentially update the max length
# move the left pointer until meeting the same letter again
# while removing from the counts on the way
# in the check the max length again and return
