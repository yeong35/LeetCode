class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = []

        for i in nums:
            if i not in temp:
                temp.append(i)
            else:
                temp.remove(i)


        return temp[0]