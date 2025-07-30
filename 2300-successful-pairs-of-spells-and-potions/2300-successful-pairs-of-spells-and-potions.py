class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def countSuccess(i, potions, threshold):
            left = 0
            right = len(potions)-1
            mid = (left+right)//2

            while left<=right:
                if potions[mid]*i < threshold:
                    left = mid+1
                elif potions[mid]*i >= threshold:
                    right = mid-1
                mid = (left+right)//2

            return len(potions)-mid-1

        potions.sort()
        result = []
        for i in spells:
            result.append(countSuccess(i, potions, success))
        
        return result