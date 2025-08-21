class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h = dict()
        stack = []

        for i in reversed(nums2):
            while stack and stack[-1] < i:
                stack.pop()
            
            if not stack:
                h[i] = -1
            else:
                h[i] = stack[-1]
            
            stack.append(i)

        ans = []
        for i in nums1:
            ans.append(h[i])

        return ans