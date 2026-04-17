class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


class Node:
    def __init__(self, is_end=False):
        self.children = {}
        self.is_end = is_end


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            print(node.children)
            if char in node.children:
                node = node.children[char]
                continue
            node.children[char] = Node()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.children
        for char in word:
            if char not in node:
                return False
            else:
                node = node[char]
        return True

    # def startsWith(self, prefix: str) -> bool:


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("peak")
obj.insert("pear")
obj.search("peak")
obj.search("peal")
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
