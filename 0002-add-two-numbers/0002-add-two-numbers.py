# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        upper = 0
        head = ListNode()
        curr = head

        while l1 or l2 or upper == 1:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0

            curr.next = ListNode((n1+n2+upper)%10)
            upper = (n1+n2+upper)//10
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None


        return head.next