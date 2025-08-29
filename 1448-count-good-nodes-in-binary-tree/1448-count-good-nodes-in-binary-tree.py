# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def validate(root, threshold):
            if not root:
                return 0
            elif root.val >= threshold:
                threshold = max(root.val, threshold)
                return 1+validate(root.left, threshold)+validate(root.right, threshold)
            else:
                return validate(root.left, threshold)+validate(root.right, threshold)
        
        return validate(root, root.val)