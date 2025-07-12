# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root, h, curr):
            nonlocal cnt

            if not root:
                return
            
            curr += root.val

            if curr == targetSum:
                cnt+=1
            
            if h[curr-targetSum] > 0:
                cnt += h[curr-targetSum]
            
            h[curr]+=1

            dfs(root.left, h, curr)
            dfs(root.right, h, curr)


            h[curr]-=1
            

        if not root:
            return 0

        cnt = 0
        h = defaultdict(int)
        dfs(root, h, 0)
        
        return cnt