class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0]*len(nums)

        cnt = 0
        mul = 1

        for i in nums:
            if i == 0:
                cnt += 1
            else:
                mul *= i

        if cnt > 1:
            return answer
        elif cnt == 1:
            for i in range(len(nums)):
                if nums[i] != 0:
                    answer[i] = 0
                else:
                    answer[i] = mul
        else:
            for i in range(len(nums)):
                answer[i] = mul//nums[i]

        return answer