class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        cnt = 0

        for i in range(n):
            for j in range(i+1, n+1):
                temp = s[i:j]
                if temp == temp[::-1]:
                    cnt+=1

        return cnt