from collections import defaultdict


class Node:
    def __init__(self):
        self.is_end = False
        self.children = defaultdict(Node)


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        m = len(board)
        n = len(board[0])
        my_trie = Trie()
        for word in words:
            my_trie.add(word)
        found = set()

        def backtrack(y, x, node, path):
            if not (0 <= y < m and 0 <= x < n):
                return

            tmp = board[y][x]
            char = board[y][x]
            board[y][x] = "#"
            if char not in node.children:
                board[y][x] = tmp
                return
            if char in node.children and node.children[char].is_end:
                word = path + char
                found.add(word)

            backtrack(y + 1, x, node.children[char], path + char)
            backtrack(y - 1, x, node.children[char], path + char)
            backtrack(y, x + 1, node.children[char], path + char)
            backtrack(y, x - 1, node.children[char], path + char)
            board[y][x] = tmp

        for y in range(m):
            for x in range(n):
                backtrack(y, x, my_trie.root, "")
        res = list(found)
        return res


board = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"],
]
words = ["oath", "pea", "eat", "rain"]
s = Solution()
s.findWords(board, words)
