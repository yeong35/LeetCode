# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def zigzag(root, isleft, cnt):
            if not root:
                return
            self.ans = max(self.ans, cnt)

            if isleft:
                zigzag(root.left, True, 1)
                zigzag(root.right, False, 1+cnt)
            else:
                zigzag(root.left, True, 1+cnt)
                zigzag(root.right, False, 1)

        zigzag(root.left, True, 1)
        zigzag(root.right, False, 1)
        
        return self.ans

