class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ans = -1
        left = 0
        right = sum(nums)

        for i in range(len(nums)):
            right -= nums[i]
            
            if left == right:
                ans = i
                break
            
            left += nums[i]
            

        return ans