class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        result = 0

        for i in cnt:
            if i+1 in nums:
                result = max(result, cnt[i]+cnt[i+1])
        
        return result