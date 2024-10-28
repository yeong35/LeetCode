class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        
        nums_length = len(nums)

        for i in range(1, nums_length):
            prefix[i] = prefix[i-1]*nums[i-1]

        for i in reversed(range(nums_length-1)):
            postfix[i] = postfix[i+1]*nums[i+1]
        

        return [i*j for i, j in zip(prefix, postfix)]