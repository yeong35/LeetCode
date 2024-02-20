class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        temp = range(len(nums)+1)

        for i in temp:
            if i not in nums:
                return i

        return len(nums)