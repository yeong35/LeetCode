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
        ListNode temp = null;

        while(next != null){
            temp = new ListNode(GCD(current.val, next.val), next);
            current.next = temp;

            current = next;
            next = next.next;
        }

        return head;
    }

    public static int GCD(int a, int b){
        int big = a > b ? a : b;
        int small = a < b ? a : b;

        for(int i = small; i>=1; i--){
            if(a%i==0 && b%i==0)
                return i;
        }

        return 1;
    }
}