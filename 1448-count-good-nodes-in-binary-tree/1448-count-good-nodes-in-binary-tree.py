# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # maximum, root
        que = [(root.val, root)]
        count = 0

        while que:
            val, curr = que.pop(0)

            if curr.val >= val:
                count +=1
                val = curr.val

            if curr.left is not None:
                que.append((val, curr.left))

            if curr.right is not None:
                que.append((val, curr.right))

        return count