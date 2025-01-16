class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:

        n = len(nums1)
        m = len(nums2)

        result = 0

        if m%2 == 1:
            for i in nums1:
                result = result^i
        
        if n%2 == 1:
            for i in nums2:
                result = result^i

        return result
        