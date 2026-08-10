# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def validPath(root, targetSum, currSum, temp):
            if not root:
                return

            currSum += root.val
            temp.append(root.val)

            # leaf node
            if not root.left and not root.right:
                if currSum==targetSum:
                    result.append(temp[:])

            if root.left:
                validPath(root.left, targetSum, currSum, temp)
            if root.right:
                validPath(root.right, targetSum, currSum, temp)

            temp.pop()
            currSum -= root.val

            return
            
        result = []
        validPath(root, targetSum, 0, [])
        return result


