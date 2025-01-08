class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        def isPrefixandSuffix(str1, str2):
            if len(str1) > len(str2):
                return False

            n = len(str1)
            
            if str1 == str2[:n] and str1==str2[-n:]:
                return True
            else:
                return False

        count = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if isPrefixandSuffix(words[i], words[j]):
                    count+=1
        return count