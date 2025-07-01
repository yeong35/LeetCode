class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        left = 0
        right = 0

        for i in range(len(flowerbed)):
            left = i-1
            right = i+1

            if (left < 0 or flowerbed[left] == 0) and (right >= len(flowerbed) or flowerbed[right] == 0) and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1

        if n < 1:
            return True
        return False