# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        levels = defaultdict(int)
        stack = [(root, 1)]

        while stack:
            curr, level = stack.pop()
            levels[level] += curr.val

            if curr.left:
                stack.append((curr.left, level+1))
            if curr.right:
                stack.append((curr.right, level+1))

        curr = float("-inf")
        result_level = 0

        print(levels)
        for i in range(1, len(levels)+1):
            if levels[i] > curr:
                curr = levels[i]
                result_level = i
        return result_level