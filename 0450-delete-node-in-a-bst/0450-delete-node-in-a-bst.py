# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minNumber(self, root):
        while root.left:
            root = root.left
        return root.val
        
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:

            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                root.val = self.minNumber(root.right)
                root.right = self.deleteNode(root.right, root.val)
        
        return root