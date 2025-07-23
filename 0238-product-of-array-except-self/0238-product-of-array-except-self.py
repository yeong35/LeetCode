class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0]*n

        curr = 1

        for i in range(n):
            curr *= nums[n-i-1]
            answer[n-i-1] = curr
        
        curr = 1

        for i in range(n):
            if i == 0:
                answer[i] = answer[i+1]
            elif i == n-1:
                answer[i] = curr
            else:
                answer[i] = curr * answer[i+1]
            curr *= nums[i]
        return answer