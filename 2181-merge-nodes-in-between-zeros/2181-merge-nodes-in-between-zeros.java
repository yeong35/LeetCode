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
    public ListNode mergeNodes(ListNode head) {
        ListNode result = new ListNode();
        ListNode prev = null;
        ListNode current = result;

        int sum = 0;

        while(head != null){
            prev = current;

            if(head.val != 0)
                sum+=head.val;
            else{
                if(sum!=0){
                    current.val = sum;
                    sum = 0;
                    current.next = new ListNode();
                    current = current.next;
                }
            }

            head = head.next;
        }
        
        prev.next = null;

        return result;
    }
}