# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maximum = float('-inf')
        curr_level = 1
        result_level = 1

        queue = [root]
        
        while queue:
            n = len(queue)

            total = 0
            for i in range(n):
                curr = queue.pop(0)
                total += curr.val

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            if total > maximum:
                maximum = total
                result_level = curr_level

            curr_level += 1




        return result_level