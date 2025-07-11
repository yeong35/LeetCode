# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(root, left, curr):
            nonlocal cnt
            if not root:
                return
            
            if left:
                dfs(root.right, False, curr+1)
                dfs(root.left, True, 1)
            else:
                dfs(root.right, False, 1)
                dfs(root.left, True, curr+1)
            
            cnt = max(cnt, curr)

        cnt = 0
        dfs(root.left, True, 1)
        dfs(root.right, False, 1)
        return cnt