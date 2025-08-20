# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        ans.next = ListNode()
        head = ans
        left = 0
        
        while l1 or l2:
            head.next = ListNode()
            head = head.next
            
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            
            head.val = (a+b+left)%10
            left = (a+b+left)//10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if left:
            head.next = ListNode()
            head = head.next
            head.val = left

        return ans.next