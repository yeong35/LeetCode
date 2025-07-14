# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root, storage):
            if not root:
                return
                
            inorder(root.left, storage)
            storage.append(root.val)
            inorder(root.right, storage)
        
        storage = []
        inorder(root,storage)
        return storage