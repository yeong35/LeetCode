# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        result = float("-inf")

        slow = head
        fast = head.next
        stack = [head.val]

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            stack.append(slow.val)
        
        while stack:
            slow = slow.next
            result = max(result, stack.pop()+slow.val)
            
        
        return result