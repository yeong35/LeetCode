# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def zigzag(root, left, curr):
            if not root: 
                return
            
            self.result = max(self.result, curr)

            if left:
                zigzag(root.left, True, 1)
                zigzag(root.right, False, curr+1)
            else:
                zigzag(root.left, True, curr+1)
                zigzag(root.right, False, 1)
        
        self.result = 0
        zigzag(root, True, self.result)
        return self.result