# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = [root]
        high = root.val
        cnt = 0

        while queue:
            n = len(queue)
            temp = high
            
            for i in range(n):
                curr = queue.pop(0)
                if curr.val <= high:
                    cnt+=1
                else:
                    temp = curr.val

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            high = temp


        return cnt