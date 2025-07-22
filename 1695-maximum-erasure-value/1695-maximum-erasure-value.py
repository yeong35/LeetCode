class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        result = 0
        curr = 0
        s = set()
        left = 0

        for right in range(len(nums)):
            while nums[right] in s:
                s.remove(nums[left])
                curr -= nums[left]
                left += 1

            s.add(nums[right])
            curr+=nums[right]
            result = max(result,curr)
            

        return result