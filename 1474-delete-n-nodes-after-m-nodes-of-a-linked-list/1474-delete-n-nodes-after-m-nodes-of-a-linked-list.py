# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        mCount = 0
        nCount = 0

        curr = head
        prev = head

        while curr:
            if mCount < m:
                mCount+=1

                prev = curr

            else:
                if nCount < n:
                    nCount+=1
                else:
                    prev.next = curr
                    prev = curr
                    
                    mCount = 1
                    nCount = 0

            curr = curr.next

        prev.next = None
        
        return head
            