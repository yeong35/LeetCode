class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def binary_search(spell, potions, success):
            left = 0
            right = len(potions)-1
            mid = (left+right)//2

            while left <= right:
                if potions[mid]*spell < success:
                    left = mid + 1
                else:
                    right = mid - 1
                mid = (left+right)//2

            return mid



        potions.sort()
        result = []
        for i in spells:
            result.append(len(potions)-binary_search(i, potions, success)-1)
        
        return result