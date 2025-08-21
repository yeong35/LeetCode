class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        h = defaultdict(int)
        cnt = 0

        for i in nums:
            if h[k-i] > 0:
                h[k-i] -= 1
                cnt += 1
            else:
                h[i]+=1
        
        return cnt