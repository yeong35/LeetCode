from collections import Counter
from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = Counter(nums)

        if n == k:
            return max(nums)
        
        candidates = []
        
        if k == 1:
            for i in nums:
                if cnt[i] == 1:
                    candidates.append(i)
            
            return max(candidates, default = -1)


        if cnt[nums[0]] == 1:
            candidates.append(nums[0])
        if cnt[nums[-1]] == 1:
            candidates.append(nums[-1])

        return max(candidates, default=-1)