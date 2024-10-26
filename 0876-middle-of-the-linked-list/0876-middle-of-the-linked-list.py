# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = 0

        current = head


        while current.next != None:
            cnt+=1
            current = current.next

        cnt /= 2

        while cnt > 0:
            head = head.next
            cnt-=1

        return head