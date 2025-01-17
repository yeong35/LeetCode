class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        
        n = len(derived)

        original = [0]*n

        for i in range(n-1):

            if derived[i] == 1:
                original[i+1] = (original[i]+1)%2
            else:
                original[i+1] = original[i]

        if original[0]^original[n-1] == derived[n-1]:
            return True
        else:
            return False