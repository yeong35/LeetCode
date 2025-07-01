class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        wordSet1 = set(word1)
        wordSet2 = set(word2)
        wordCount1 = sorted(Counter(word1).values())
        wordCount2 = sorted(Counter(word2).values())
        return wordSet1 == wordSet2 and wordCount1 == wordCount2
        