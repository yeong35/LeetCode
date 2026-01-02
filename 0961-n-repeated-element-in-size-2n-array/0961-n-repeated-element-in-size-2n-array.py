class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)//2

        dictionary = defaultdict(int)

        for i in nums:
            dictionary[i]+=1

            if dictionary[i] == n:
                return i