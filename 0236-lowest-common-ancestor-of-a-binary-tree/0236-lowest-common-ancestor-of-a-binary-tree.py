# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ancestor = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def find_value(root, p, q):
            if not root:
                return False
            

            left = find_value(root.left, p, q)
            right = find_value(root.right, p, q)
            mid = True if p == root or q == root else False

            if mid + left + right > 1:
                self.ancestor = root
            
            
            if left or right or mid:
                return True
            return False

        find_value(root, p, q)

        return self.ancestor