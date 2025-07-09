class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        fliped = 0
        result = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                fliped+=1

            while fliped > k:
                if nums[left] == 0:
                    fliped -= 1
                left += 1
            
            result = max(result, right-left+1)
        
        return result