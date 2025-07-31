class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def count(piles, consume):
            hour = 0

            for i in piles:
                if i%consume == 0:
                    hour += i//consume
                else:
                    hour += i//consume + 1

            return hour
        
        def binary_search(right, h):
            left = 1
            mid = (left+right)//2
            while left <= right:
                time = count(piles, mid)
                # print(mid, time)
                if h < time:
                    left = mid + 1
                elif h >= time:
                    right = mid - 1
                
                mid = (left+right)//2

            return mid+1

        piles.sort()
        return binary_search(piles[-1], h)            
            
