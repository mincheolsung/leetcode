class TrieNode:
    def __init__(self, val="", isEnd=0):
        self.val = val
        self.children = defaultdict(TrieNode)
        self.isEnd = isEnd

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for s in word:
            cur = cur.children[s]
            if cur.val != s:
                cur.val = s
        cur.isEnd = 1

    def search(self, word: str) -> bool:
        cur = self.root
        for s in word:
            cur = cur.children[s]
            if cur.val != s:
                return False
        return cur.isEnd == 1

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for s in prefix:
            cur = cur.children[s]
            if cur.val != s:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)