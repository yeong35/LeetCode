class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = float('-inf')
        temp = 0

        for i in range(1, len(nums)):
            temp+=nums[i-1]
            if nums[i-1] >= nums[i]:
                result = max(result, temp)
                temp = 0

        return max(result, temp+nums[-1])