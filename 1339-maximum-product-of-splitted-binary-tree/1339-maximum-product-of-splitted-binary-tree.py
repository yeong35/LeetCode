# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        subtotal = []
        modulo = pow(10,9)+7

        def subsum(root):
            if not root:
                return 0
            
            left = subsum(root.left)
            right = subsum(root.right)

            total = root.val+left+right

            subtotal.append(total)

            return total

        total = subsum(root)
        result = 0
        for i in subtotal:
            result = max(result, i*(total-i))

        return result%modulo