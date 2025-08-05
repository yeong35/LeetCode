# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        stack = [(root, 0)]

        while stack:
            curr, level = stack.pop()

            if len(result) == level:
                result.append(curr.val)

            if curr.left:
                stack.append((curr.left, level+1))
            if curr.right:
                stack.append((curr.right, level+1))

        
        return result

