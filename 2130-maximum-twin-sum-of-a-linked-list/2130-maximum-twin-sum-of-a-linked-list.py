# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def reverseNode(head):
            if not head or not head.next:
                return head
            
            p = reverseNode(head.next)
            head.next.next = head
            head.next = None

            return p
        
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        h2 = reverseNode(slow.next)
        slow.next = None
        h1 = head
        
        result = float('-inf')

        while h1 and h2:
            result = max(result, h1.val+h2.val)
            h1 = h1.next
            h2 = h2.next
        
        return result

