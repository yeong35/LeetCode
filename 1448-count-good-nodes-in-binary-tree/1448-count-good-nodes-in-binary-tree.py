# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def count_good_nodes(root, threshold):
            if not root:
                return
            
            if root.val >= threshold:
                self.result+=1
            
            count_good_nodes(root.left, max(threshold, root.val))
            count_good_nodes(root.right, max(threshold, root.val))
        
        if not root:
            return 0

        self.result = 0
        count_good_nodes(root, root.val)
        return self.result