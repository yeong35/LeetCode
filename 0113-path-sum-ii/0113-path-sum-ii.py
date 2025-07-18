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
        def dfs(root, storage, targetSum):
            if not root:
                return
            
            storage.append(root.val)
            targetSum -= root.val

            if not root.left and not root.right and targetSum == 0:
                self.result.append(list(storage))
            
            dfs(root.left, storage, targetSum)
            dfs(root.right, storage, targetSum)

            storage.pop()

        dfs(root, [], targetSum)

        return self.result