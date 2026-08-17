# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def checkCandidate(root, subRoot):
            
            queue1 = [root]     
            queue2 = [subRoot]

            while queue1 and queue2:
                curr1 = queue1.pop(0)
                curr2 = queue2.pop(0)

                if curr1.val != curr2.val:
                    return False
                    
                if curr1.left and curr2.left:
                    queue1.append(curr1.left)
                    queue2.append(curr2.left)
                elif (curr1.left and not curr2.left) or (not curr1.left and curr2.left):
                    return False

                if curr1.right and curr2.right:
                    queue1.append(curr1.right)
                    queue2.append(curr2.right)
                elif (curr1.right and not curr2.right) or (not curr1.right and curr2.right):
                    return False

            return len(queue1) == len(queue2)
        
        if not root and not subRoot:
            return True
        if (not root and subRoot) or (root and not subRoot):
            return False 

        queue = [root]

        while queue:
            curr = queue.pop(0)

            if curr.val == subRoot.val:
                if checkCandidate(curr, subRoot):
                    return True

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        
        return False
