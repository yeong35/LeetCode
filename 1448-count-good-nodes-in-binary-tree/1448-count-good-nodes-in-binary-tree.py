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
            
            mid = 1 if root.val >= threshold else 0
            left = validate(root.left, max(threshold, root.val))
            right = validate(root.right, max(threshold, root.val))

            return mid+left+right

        return validate(root, root.val)