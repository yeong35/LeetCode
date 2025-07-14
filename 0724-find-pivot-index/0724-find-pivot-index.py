class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        past = 0

        for i in range(len(nums)):
            if past*2 == total-nums[i]:
                return i
            past += nums[i]
        
        return -1