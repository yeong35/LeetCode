class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dup = sorted(nums)
        ans = []

        for i in nums:
            ans.append(bisect.bisect_left(dup, i))
        
        return ans