# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp = []
        
        while headA != None:
            temp.append(headA)
            headA = headA.next

        print(temp)
        while headB != None:
            if headB in temp:
                return headB
            headB = headB.next
        return None