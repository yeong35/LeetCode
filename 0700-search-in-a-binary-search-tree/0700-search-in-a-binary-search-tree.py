# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root.val == val:
            return root
        else:
            search_left = self.searchBST(root.left, val) if root.left is not None else None
            search_right = self.searchBST(root.right, val) if root.right is not None else None
            
            result = None
            if search_left is not None:
                result = search_left
            elif search_right is not None:
                result = search_right

            return result