class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:

    def __init__(self):
        self.words = {}

    def insert(self, word: str) -> None:
        self.words[word] = "cool"

    def search(self, word: str) -> bool:
        if self.words.get(word):
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        return len([word for word in self.words if word.startswith(prefix)]) > 0


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
