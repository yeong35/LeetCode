class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        h1 = Counter(word1)
        h2 = Counter(word2)

        return sorted(h1.keys()) == sorted(h2.keys()) and sorted(h1.values()) == sorted(h2.values())