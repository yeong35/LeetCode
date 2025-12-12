class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0

        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        nums2.reverse()

        for i in range(len(nums1)):
            result += nums1[i]*nums2[i]

        return result
        