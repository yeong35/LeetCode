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
    public int[] nodesBetweenCriticalPoints(ListNode head) {
        ListNode prev = head;
        head = head.next;
        ListNode next = head.next;

        int[] result = {-1, -1};

        ArrayList<Integer> criticals = new ArrayList<>();
        int min = 100000;
        int idx = 1;

        while(next != null){
            if((prev.val < head.val && next.val < head.val) || (prev.val > head.val && next.val > head.val)){
                criticals.add(idx);
            }

            prev = head;
            head = next;
            next = next.next;
            idx++;

        }

        if(criticals.size() < 2)
            return result;

        for(int i = 1; i<criticals.size(); i++)
            min = Math.min(min, criticals.get(i)-criticals.get(i-1));

        result[0] = min;
        result[1] = criticals.get(criticals.size()-1) - criticals.get(0);

        return result;
    }
}