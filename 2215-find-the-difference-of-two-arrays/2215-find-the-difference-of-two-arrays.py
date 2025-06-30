class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        result1 = set()
        result2 = set()

        for i in range(len(nums1)):
            if nums1[i] not in set2:
                result1.add(nums1[i])
        for i in range(len(nums2)):
            if nums2[i] not in set1:
                result2.add(nums2[i])

        return [list(result1), list(result2)]