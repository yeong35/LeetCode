# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findmin(root):
            value = root.val
            while root:
                value = root.val
                root = root.left
            return value           
        if not root:
            return None

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                root = None
            elif not root.right:
                root = root.left
            else:
                low = findmin(root.right)
                root.val = low
                root.right = self.deleteNode(root.right, root.val)

        return root