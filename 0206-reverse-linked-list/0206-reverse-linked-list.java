/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode reversedHead = new ListNode();
        ListNode temp = null;

        while(head != null){
            
            temp = new ListNode();
            temp.val = head.val;

            if(reversedHead.next == null)
                reversedHead.next = temp;
            else{
                temp.next = reversedHead.next;
                reversedHead.next = temp;
            }

            head = head.next;
        }

        return reversedHead.next;
    }
}