class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}

        for i in s:
            if i not in sDict:
                sDict[i] = 1
            else:
                sDict[i] += 1

        for i in t:
            if i not in tDict:
                tDict[i] = 1
            else:
                tDict[i] += 1


        if sDict == tDict:
            return True
        else:
            return False