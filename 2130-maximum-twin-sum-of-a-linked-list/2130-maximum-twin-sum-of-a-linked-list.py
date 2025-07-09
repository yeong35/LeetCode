# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head

        temp = []

        while fast and fast.next:
            temp.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        for i in range(len(temp)):
            temp[-i-1]+=slow.val
            slow = slow.next

        return max(temp)