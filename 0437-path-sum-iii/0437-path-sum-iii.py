# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cnt = 0
        def recursion(root, h, curr):
            nonlocal cnt
            if not root:
                return
            
            curr += root.val

            if curr == targetSum:
                cnt+=1
            if h[curr-targetSum] > 0:
                cnt += h[curr-targetSum]

            h[curr] += 1

            recursion(root.left, h, curr)
            recursion(root.right, h, curr)

            h[curr] -= 1

        h = defaultdict(int)
        recursion(root, h, 0)
        return cnt