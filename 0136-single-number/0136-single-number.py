class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}

        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] = count[i]+1

        for key, value in count.items():
            print(key, value)
            if value==1:
                return key

