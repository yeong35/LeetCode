class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = 2**31 - 1
        second = 2**31 - 1
        
        for i in nums:
            print(first, second)
            if i < first:
                first = i
            elif i > first and i < second:
                second = i
            elif i > second:
                return True

        return False