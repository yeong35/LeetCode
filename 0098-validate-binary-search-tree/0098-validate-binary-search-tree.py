# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, high, low):
            if not root:
                return True
            if root.val >= high or root.val <= low:
                return False
            
            return validate(root.left, root.val, low) and validate(root.right, high, root.val)
        
        return validate(root, math.inf, -math.inf)