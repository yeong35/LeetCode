class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True
    
    def search(self, word: str):
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return curr.end
    
    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return True

    def recommend_upto_three(self, prefix):
        if not self.startsWith(prefix):
            return []
        
        recommend = []
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                break
            curr = curr.children[c]

        stack = [[curr, prefix]]
        
        while stack:
            c, s = stack.pop()

            if c.end:
                recommend.append(s)

            for neighbor in c.children:
                stack.append([c.children[neighbor], s+neighbor])
        recommend.sort()
        
        return recommend[:3]

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()

        for i in products:
            trie.insert(i)
            
        ans = []

        for i in range(1, len(searchWord)+1):
            ans.append(trie.recommend_upto_three(searchWord[:i]))

        return ans