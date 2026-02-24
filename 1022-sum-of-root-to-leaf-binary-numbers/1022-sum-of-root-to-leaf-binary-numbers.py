# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        result = 0
        def construct(root, total):
            nonlocal result

            if not root:
                return
            
            concat = total + str(root.val)
            construct(root.left, concat)
            construct(root.right, concat)

            if not root.left and not root.right:
                result += int(concat, 2)
        
        construct(root, "")
        return result