# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def findleafs(root):
            leafs = []

            stack = [root]

            while stack:
                curr = stack.pop()

                if not curr.left and not curr.right:
                    leafs.append(curr.val)
                
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
            
            return leafs


        leafs1 = findleafs(root1)
        leafs2 = findleafs(root2)

        return leafs1 == leafs2