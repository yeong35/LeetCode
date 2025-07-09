# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        cnt = 0

        while curr:
            curr = curr.next
            cnt += 1
        
        curr = head
        i = 0

        while i < cnt//2-1:
            curr = curr.next
            i += 1

        if curr.next:
            curr.next = curr.next.next
        else:
            head = None    

        return head
