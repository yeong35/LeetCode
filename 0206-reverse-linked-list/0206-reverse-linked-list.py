# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        prev, curr, future = None, head, head.next

        while curr:
            prev, curr.next, future = curr, prev, curr.next
            curr = future

        return prev
