class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        idx1 = 0
        idx2 = 0
        print(s, t)
        while idx1<len(s) and idx2<len(t):
            
            temp1 = s[idx1] if idx1<len(s) else ""
            temp2 = t[idx2] if idx2<len(t) else ""

            if temp1==temp2:
                idx1+=1
                idx2+=1
            else:
                idx2+=1
            
        return idx1 == len(s)