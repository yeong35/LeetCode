# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def recursion(root, values):
            if not root:
                return
            
            values.append(root.val)
            if not root.left and not root.right:
                if sum(values) == targetSum:
                    self.result.append(list(values))
                
            recursion(root.left, values)
            recursion(root.right, values)

            values.pop()
        
        recursion(root, [])
        return self.result