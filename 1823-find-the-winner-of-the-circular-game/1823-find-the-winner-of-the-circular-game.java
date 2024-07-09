class Solution {
    class Node{
        int val;
        Node next = null;

        public Node(int val){
            this.val = val;
        }

        public Node(int val, Node next){
            this.val = val;
            this.next = next;
        }
    }

    public int findTheWinner(int n, int k) {
        Node head = new Node(1);
        Node prev = null;
        Node temp = head;

        int cnt = 1;

        for(int i = 2; i<=n; i++){
            temp.next = new Node(i);
            temp = temp.next;
        }

        prev = temp;
        temp.next = head;

        while(head.next != null){
            if(cnt == k){
                System.out.println(prev.val +" "+ head.val + " " + head.next.val);
                prev.next = head.next;

                if(head == head.next)
                    return head.val;

                cnt = 0;
            }
            else
                prev = head;
            head = head.next;
            cnt++;
        }

        return head.val;
    }
}