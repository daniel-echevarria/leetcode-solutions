from collections import deque


class Node:
    def __init__(self, word, depth=0):
        self.word = word
        self.depth = depth


def isOneLetterAway(word1, word2):
    if len(word1) == 1:
        return True
    differ = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            differ += 1
    return differ == 1


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        root = Node(beginWord)
        queue = deque([root])
        visited = set()
        while queue:
            node = queue.popleft()
            word = node.word
            if word in visited:
                continue
            if word == endWord:
                return node.depth + 1
            visited.add(word)
            for w in wordList:
                if w not in visited and isOneLetterAway(word, w):
                    queue.append(Node(w, (node.depth + 1)))
        return 0
