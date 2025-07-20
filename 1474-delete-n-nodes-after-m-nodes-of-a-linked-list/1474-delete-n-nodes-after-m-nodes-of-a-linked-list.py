# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        if not head:
            return head
        
        mCount = 1
        nCount = 0

        curr = head
        nNode = head

        while curr:
            if mCount < m:
                mCount+=1
                
                curr = curr.next
                nNode = nNode.next
            elif nCount <= n:
                nCount += 1
                
                curr = curr.next
            else:
                mCount = 1
                nCount = 1

                nNode.next = curr
                curr = curr.next
                nNode = nNode.next
        
        nNode.next = None

        return head