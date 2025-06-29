class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        used = 0
        result = 0

        for i in range(len(nums)):
            print(left, i, used)
            if nums[i] == 0:
                if used < k:
                    used+=1
                else:
                    while used == k:
                        if nums[left] == 0:
                            used -=1
                        left += 1
                    used += 1 

            result = max(result, i-left+1)
        
        return result