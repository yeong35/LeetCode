class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        check = defaultdict(int)

        ans = []

        for i in range(n):
            check[nums[i]] += 1
            if check[nums[i]] == 2:
                ans.append(nums[i])

        for i in range(n):
            if check[i+1] == 0:
                ans.append(i+1)

        return ans
        
