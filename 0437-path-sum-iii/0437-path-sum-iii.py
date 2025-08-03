# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cnt = 0
        def validate(root, h, curr):
            nonlocal cnt
            if not root:
                return
            
            curr += root.val
            if curr == targetSum:
                cnt += 1
            
            cnt += h[curr-targetSum]
            h[curr] += 1

            validate(root.left, h, curr)
            validate(root.right, h, curr)
            
            h[curr] -=1
            
        validate(root, defaultdict(int), 0)

        return cnt
