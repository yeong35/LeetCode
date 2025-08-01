# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = [root]
        return_index = 0
        idx = 0
        big = float('-inf')

        while q:
            n = len(q)
            temp = 0

            for i in range(n):
                curr = q.pop(0)
                temp += curr.val

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
            if temp > big:
                return_index = idx
                big = temp
            idx+=1
        return return_index+1