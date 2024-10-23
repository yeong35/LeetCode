class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        cnt = 0

        for i in range(len(words)):
            word = words[i]

            for j in range(i+1, len(words)):
                # print(word, words[j], words[j][:len(word)], words[j][-len(word):])
                if len(word) <= len(words[j]) :
                    if words[j][:len(word)] == word and words[j][-len(word):] == word:
                        cnt += 1
        
        return cnt