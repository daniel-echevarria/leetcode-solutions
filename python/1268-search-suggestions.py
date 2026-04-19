class TrieNode:
    def __init__(self, value=""):
        self.value = value
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.res = []

    def insertWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
        node.is_end = True

    def getWordsStartingWith(self, prefix, current_word=""):
        self.res = []
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            if node.is_end:
                self.res.append(current_word)
            node = node.children[char]
            current_word += char
        if node.is_end:
            self.res.append(current_word)
        self.getWords(node, prefix)
        return sorted(self.res)[:3]

    def getWords(self, node, current_word):
        for char in node.children:
            if node.children[char].is_end:
                self.res.append(current_word + char)
            self.getWords(node.children[char], current_word + char)


class Solution:
    def suggestedProducts(
        self, products: list[str], searchWord: str
    ) -> list[list[str]]:
        trie = Trie()
        for p in products:
            trie.insertWord(p)

        res = []
        for i in range(1, len(searchWord) + 1):
            res.append(trie.getWordsStartingWith(searchWord[:i]))
        return res


products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
searchWord = "mouse"
s = Solution()

print(s.suggestedProducts(products, searchWord))
