class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)

        optimal = right

        while left < right:
            mid = (left+right)//2

            cnt = 0

            for pile in piles:
                cnt += math.ceil(pile/mid)

            print(mid, cnt)

            if cnt > h:
                left = mid+1
            else:
                right = mid
                optimal = mid
            
        return optimal