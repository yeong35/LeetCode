class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def binarySearch(spell, potions, threshold):
            left = 0
            right = len(potions)

            while left<right:
                mid = (left+right)//2
                if potions[mid]*spell >= threshold:
                    right = mid
                else:
                    left = mid+1

            return left


        potions.sort()

        ans = []
        for i in spells:
            ans.append(len(potions)-binarySearch(i, potions, success))

        return ans