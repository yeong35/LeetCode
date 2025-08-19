class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = []
        d = []

        for i in range(len(senate)):
            if senate[i] == 'R':
                r.append(i)
            else:
                d.append(i)


        while r and d:
            s1 = r.pop(0)
            s2 = d.pop(0)
            
            if s1 < s2:
                r.append(len(senate)+s1)
            else:
                d.append(len(senate)+s2)
        
        if r:
            return "Radiant"
        else:
            return "Dire"