class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []

        for i in range(1, n+1):
            ans.append(nums[i-1])
            ans.append(nums[n+i-1])

        return ans