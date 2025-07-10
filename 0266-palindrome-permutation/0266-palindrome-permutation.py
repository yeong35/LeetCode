class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        temp = Counter(s)
        oneCounter = 0

        for i in temp:
            if temp[i]%2 == 1:
                oneCounter+=1
        
        return oneCounter < 2
        