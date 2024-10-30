class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        nums_map = {}

        for i in nums:
            if i in nums_map:
                nums_map[i] += 1
            else:
                nums_map[i] = 1

        result = -1

        for key, value in nums_map.items():
            if value == 1 and result < key:
                result = key

        return result