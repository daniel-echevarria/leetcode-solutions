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


t = Trie()
t.add("peak")
t.add("hey")
t.add("cool")
print(t.search("hey"))
print(t.search("coo"))
print(t.search("cool"))
# class Solution:
#     def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:

# # Algo
# # Build a Trie for each word in words


# board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
# words = ["oath","pea","eat","rain"]
# s = Solution()
# s.findWords()
