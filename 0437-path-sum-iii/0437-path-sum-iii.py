def pathSequence(node, accum):
    if node == None:
        return 0
    
    count = 0
    if accum == node.val:
        count += 1
    
    count += pathSequence(node.left, accum-node.val)+pathSequence(node.right, accum-node.val)

    return count
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root == None:
            return 0
        
        return pathSequence(root, targetSum)+self.pathSum(root.left, targetSum)+self.pathSum(root.right, targetSum)
