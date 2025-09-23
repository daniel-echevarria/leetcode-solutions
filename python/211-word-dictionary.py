class Node:
    def __init__(self):
        self.is_end = False
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in enumerate(word):
            if char in node.children:
                node = node.children[char]
                continue
            node.children[char] = Node()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        jumped = []
        for char in word:
            if char == "." and not jumped:
                for values in node.children.values():
                    jumped.append(values.children)

            else:
                if char not in node.children:
                    return False
                node = node.children[char]
            jumped = False
        return node.is_end


wordDictionary = WordDictionary()
print(
    wordDictionary.addWord("bad"),
    wordDictionary.addWord("dad"),
    wordDictionary.addWord("mad"),
    wordDictionary.search("pad"),
    wordDictionary.search("bad"),
    wordDictionary.search(".ad"),
    wordDictionary.search("b.."),
)
