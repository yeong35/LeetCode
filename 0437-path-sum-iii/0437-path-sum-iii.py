# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def pathCheck(root, h, curr):
            nonlocal cnt 

            if not root:
                return

            curr += root.val

            h[curr] += 1
            cnt += h[curr-targetSum]

            pathCheck(root.left, h, curr)
            pathCheck(root.right, h, curr)

            h[curr] -= 1
        
        
        h = defaultdict(int)
        h[0] += 1
        cnt = 0

        pathCheck(root, h, 0)

        return cnt