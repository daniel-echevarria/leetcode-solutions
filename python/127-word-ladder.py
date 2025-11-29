from collections import deque, defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        wordList = set(wordList)
        wordList.add(beginWord)

        def get_neighbors(word):
            neighbors = []
            for i in range(len(word)):
                res = word[:i] + "?" + word[i + 1 :]
                neighbors.append(res)
            return neighbors

        wildcard_buckets = defaultdict(list)
        for word in wordList:
            for wildcard in get_neighbors(word):
                wildcard_buckets[wildcard].append(word)

        neighbors_map = defaultdict(list)
        for word in wordList:
            for wild in get_neighbors(word):
                neighbors_map[word] += wildcard_buckets[wild]

        queue = deque([(beginWord, 1)])
        visited = set()

        while queue:
            current, distance = queue.popleft()
            if current in visited:
                continue
            if current == endWord:
                return distance
            for n in neighbors_map[current]:
                queue.append((n, distance + 1))
            visited.add(current)

        return 0


s = Solution()
# begin = "hit"
# end = "cog"
# wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
# begin = "hot"
# end = "dog"
# wordList = ["hot", "dog", "cog", "pot", "dot"]
begin = "a"
end = "c"
wordList = ["a", "b", "c"]

print(s.ladderLength(begin, end, wordList))

# Given two words and a list of words, return the minimum number of steps
# from word 1 to word2 given that the in between words must exist in the word list
# and that only one letter at the time can be changed

# Algo:
# For each word, make a map of all the possible one letter transformations of the word
# for example hot would map to ?ot h?t ho?
# Declare a set of visited
# Then launch a dfs from the first word and for each neighbor
# look for a match in the wordlist, if no match is found return 0
# otherwise add one to count and recurse
# if the current_word word equals the endWord, update minDistance to the min of current_wordDistance
# and minDistance
