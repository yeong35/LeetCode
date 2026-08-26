class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        result = int(s, 2)

        left = 0

        for right in range(len(s)):
            if s[right] == "1":
                k -= 1
            
            while k < 0:
                if s[left] == "1":
                    k += 1
                left += 1
            
            if k == 0:
                temp = int(s[left:right+1], 2)
                result = min(temp, result)
        
        if k > 0:
            return ""

        return bin(result)[2:]