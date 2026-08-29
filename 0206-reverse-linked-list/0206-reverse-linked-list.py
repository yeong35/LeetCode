# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def recursive(root, past):
            if not root:
                return past

            temp = root.next
            root.next = past

            return recursive(temp, root)
        
        return recursive(head, None)