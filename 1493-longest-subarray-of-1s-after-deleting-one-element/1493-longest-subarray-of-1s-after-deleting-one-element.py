class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cnt = 1
        left = 0
        length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                cnt -= 1

            while cnt < 0:
                if nums[left] == 0:
                    cnt += 1
                left += 1
            
            length = max(length, right-left+1)

        return length-1