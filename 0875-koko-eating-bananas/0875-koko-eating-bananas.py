class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        mid = (left+right)//2

        while left<right:
            cnt = 0

            for i in piles:
                cnt += math.ceil(i/mid)
            if cnt > h:
                left = mid+1
            else:
                right = mid

            mid = (left+right)//2
            
        
        return mid