class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        memo = {}

        def dfs(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]

            for word in wordDict:
                if s.startswith(word, i):
                    if dfs(i + len(word)):
                        memo[i] = True
                        return True

            memo[i] = False
            return False

        return dfs(0)


sol = Solution()
s = "leetcode"
wordDict = ["leet", "code"]
# s = "cars"
# wordDict = ["car", "ca", "rs"]
# s = "ddadddbdddadd"
# wordDict = ["dd", "ad", "da", "b"]
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
print(sol.wordBreak(s, wordDict))


# Brute force:
# Iterate through the wordDict array, if the word is a substring of s
# recursively break the word. If current string  is empty return true
# after iteration return false
