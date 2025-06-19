class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[idx]
                nums[idx] = nums[i]
                nums[i] = temp
                idx+=1
        
        return nums
        