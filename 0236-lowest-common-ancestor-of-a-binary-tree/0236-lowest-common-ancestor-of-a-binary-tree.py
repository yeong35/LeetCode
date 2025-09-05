# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def search(root, p, q):
            if not root:
                return 0
            
            mid = 1 if root == p or root == q else 0
            left = search(root.left, p, q)
            right = search(root.right, p, q)

            if mid+left+right > 1:
                self.ans = root
            
            return mid or left or right
            
        search(root, p, q)

        return self.ans