class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result = 0
        curr = 0
        for i in nums[:k]:
            curr += i
        result = curr

        for i in range(k, len(nums)):
            curr += nums[i]
            curr -= nums[i-k]

            result = max(result, curr)
        
        return result/k
