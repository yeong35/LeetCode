# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        stack = [(-1, 0, root)]
        longest = 0

        # 0 left, 1 right
        while stack:
            direction, cnt, curr = stack.pop()

            longest = max(longest, cnt)
            
            # first
            if direction == -1:
                if curr.left:
                    stack.append((0, cnt+1, curr.left))
                if curr.right:
                    stack.append((1, cnt+1, curr.right))
            # from left
            elif direction == 0:
                if curr.left:
                    stack.append((0, 1, curr.left))
                if curr.right:
                    stack.append((1, cnt+1, curr.right))
            # from right
            else:
                if curr.left:
                    stack.append((0, cnt+1, curr.left))
                if curr.right:
                    stack.append((1, 1, curr.right))

        return longest