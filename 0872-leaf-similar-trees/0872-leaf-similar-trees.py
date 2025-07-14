# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        stack = [root1]
        leaf1 = []
        leaf2 = []

        while stack:
            curr = stack.pop()

            if curr.left is None and curr.right is None:
                leaf1.append(curr.val)
                continue

            if curr.left:
                stack.append(curr.left)

            if curr.right:
                stack.append(curr.right)

        stack.append(root2)

        while stack:
            curr = stack.pop()

            if curr.left is None and curr.right is None:
                leaf2.append(curr.val)
                continue

            if curr.left:
                stack.append(curr.left)

            if curr.right:
                stack.append(curr.right)

        return leaf1 == leaf2