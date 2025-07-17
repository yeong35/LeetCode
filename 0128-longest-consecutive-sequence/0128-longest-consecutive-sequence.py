class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h = set(nums)
        consecutive = 0
        result = 0

        for i in nums:
            curr = i
            consecutive = 0
            if curr-1 in h:
                continue
            
            while curr in h:
                h.remove(curr)
                consecutive += 1
                curr += 1
                
            result = max(result, consecutive)

        
        return result