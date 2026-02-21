from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        indices = defaultdict(list)
        for i, char in enumerate(s):
            indices[char].append(i)

        max_string = 0

        for letter, idxs in indices.items():
            for idx in idxs:
                if n - idx < max_string:
                    continue
                r = idx
                tokens = k
                while r < n and tokens > -1:
                    if s[r] == letter:
                        r += 1
                        continue
                    tokens -= 1
                    r += 1
                total_other_letters = n - len(indices[letter])
                possible_additional_perms = min(total_other_letters, tokens)
                curr_max = r - idx + possible_additional_perms
                max_string = max(max_string, curr_max)
        return max_string


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        most_present_char = s[0]
        most_present_count = 1
        counts = {most_present_char: most_present_count}
        max_length = 1
        for r in range(1, len(s)):
            char = s[r]
            counts[char] = counts.get(char, 0) + 1
            if counts[char] > most_present_count:
                most_present_char = char
                most_present_count = counts[char]
            window_size = r - l + 1
            if window_size - most_present_count > k:
                counts[s[l]] -= 1
                l += 1
                window_size -= 1
            max_length = max(max_length, window_size)
        return max_length


s = Solution()
# st = "ABAB"
# k = 2
# st = "ABABCCABCC"
# k = 2
st = "AABABBA"
k = 1
print(s.characterReplacement(st, k))

# Algo, iterate through the string
# make a map of all the indices for each char
# then for each char try to build the longest possible string by sliding
# a window using tokens when the char is not the target
# return the longest possible window
