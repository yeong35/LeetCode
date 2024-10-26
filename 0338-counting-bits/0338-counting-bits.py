class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0, 1]

        if n < 2:
            return ans[:n+1]
        
        power = 2
        current = 0

        for i in range(2, n+1):
            if power == current:
                power *= 2
                current = 0

            if current == 0:
                ans.append(1)
            else:
                ans.append(ans[power]+ans[i-power])
            
            current += 1

        
        return ans