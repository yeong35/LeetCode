class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root

        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
            curr.words.append(word)

    def recommend(self, word):
        temp = []

        curr = self.root

        for i in word:
            if i not in curr.children:
                return []
            curr = curr.children[i]
                
        return curr.words[:3]


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans = []
        trie = Trie()
        products.sort()
        for product in products:
            trie.insert(product)
        
        temp = ''
        for i in searchWord:
            temp += i
            ans.append(trie.recommend(temp))

        return ans