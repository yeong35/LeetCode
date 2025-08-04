class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        h = defaultdict(int)
        s = set()
        ans = 0

        left = 0
        for right in range(len(fruits)):
            h[fruits[right]]+=1
            s.add(fruits[right])
            
            while len(s) > 2:
                h[fruits[left]]-=1
                if h[fruits[left]]==0:
                    s.remove(fruits[left])
                left+=1
            
            ans = max(ans, right-left+1)
        
        return ans