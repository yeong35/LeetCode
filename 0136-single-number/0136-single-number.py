class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = nums[0]

        for i in nums[1:]:
            temp = temp^i

        return temp