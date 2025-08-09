class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        elif len(nums) == 3:
            return max(nums[1], nums[0]+nums[2])
        
        arr = nums[:3]
        arr[2] = nums[0]+nums[2]

        for i in range(3, len(nums)):
            arr.append(nums[i]+max(arr[i-3], arr[i-2]))

        return max(arr[-1], arr[-2])