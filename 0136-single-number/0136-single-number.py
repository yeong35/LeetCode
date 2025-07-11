class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        checker = Counter(nums)

        for i in checker:
            if checker[i] == 1:
                return i
        
        return -1