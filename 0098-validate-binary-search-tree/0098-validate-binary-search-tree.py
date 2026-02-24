# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checker(root, small, big):
            if not root:
                return True
            
            left = True
            right = True
            curr = True if root.val > small and root.val < big else False
            
            if root.left:
                left = checker(root.left, small, root.val)
            if root.right:
                right = checker(root.right, root.val, big)

            return left and right and curr

        return checker(root, float('-inf'), float('inf'))
            

        