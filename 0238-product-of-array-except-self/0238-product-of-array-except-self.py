class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt = 0
        mul = 1

        ans = [0]*n

        for i in range(n):
            if nums[i] == 0:
                cnt += 1
            else:
                mul*=nums[i]
                
        if cnt > 1:
            return ans
        elif cnt == 1:
            for i in range(n):
                if nums[i] == 0:
                    ans[i] = mul
                else:
                    ans[i] = 0
        else:
            for i in range(n):
                ans[i] = mul//nums[i]
        return ans