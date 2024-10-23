class Solution:
    def countKeyChanges(self, s: str) -> int:
        
        s = s.lower()

        cnt = 0
        current = s[0]

        for i in s:
            if current != i:
                cnt += 1
                current = i

        return cnt