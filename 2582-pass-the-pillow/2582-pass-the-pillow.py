class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        forward = True
        person = 1
        sec = 0

        while sec < time:
            if forward:
                person+=1
            else:
                person-=1
            
            if person == n or person==1:
                forward = not forward
            
            sec+=1
        
        return person