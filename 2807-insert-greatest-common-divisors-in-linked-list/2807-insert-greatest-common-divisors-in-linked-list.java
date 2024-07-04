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
    public ListNode insertGreatestCommonDivisors(ListNode head) {
        ListNode next = head.next;
        ListNode current = head;

        while(next != null){
            current.next = new ListNode(GCD(current.val, next.val), next);

            current = next;
            next = next.next;
        }

        return head;
    }

    private int GCD(int a, int b){
        int min = Math.min(a,b);

        for(int i = min; i>=1; i--){
            if(a%i==0 && b%i==0)
                return i;
        }

        return 1;
    }
}