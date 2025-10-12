from collections import deque


class Node:
    def __init__(self):
        self.is_end = False
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
                continue
            node.children[char] = Node()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:

        def dfs(node, i):
            if i == len(word):
                return node.is_end

            char = word[i]

            if char == ".":
                for ch in node.children.values():
                    if dfs(ch, i + 1):
                        return True
                return False
            if char in node.children:
                return dfs(node.children[char], i + 1)
            return False

        return dfs(self.root, 0)


wordDictionary = WordDictionary()
print(
    wordDictionary.addWord("bad"),
    wordDictionary.addWord("dad"),
    wordDictionary.addWord("mad"),
    wordDictionary.search("pad"),
    wordDictionary.search("bad"),
    wordDictionary.addWord("mado"),
    wordDictionary.search(".ado"),
    wordDictionary.search("b.."),
)
