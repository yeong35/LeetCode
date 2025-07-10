class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr = 0
        cnt = 0
        h = defaultdict(int)

        for i in nums:
            curr += i
            
            if curr == k:
                cnt += 1
                
            if h[curr-k] > 0:
                cnt += h[curr-k]
            
            h[curr]+=1
        
        return cnt