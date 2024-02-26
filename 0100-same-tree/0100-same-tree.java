/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {

        Queue<TreeNode> que = new LinkedList<>();

        if(p == null && q == null)
            return true;

        TreeNode temp_p = p;
        TreeNode temp_q = q;

        que.add(p);
        que.add(q);

        while(!que.isEmpty()){
            temp_p = que.poll();
            temp_q = que.poll();
            // current node check
            if((temp_p != null && temp_q == null) || (temp_p == null && temp_q != null))
                return false;

            // next node check
            if(temp_p.val != temp_q.val)
                return false;
            else{
                if(temp_p.left != null && temp_q.left != null){
                    que.add(temp_p.left);
                    que.add(temp_q.left);
                }
                else if((temp_p.left != null && temp_q.left == null) || (temp_p.left == null && temp_q.left != null))
                    return false;

                if(temp_p.right != null && temp_q.right != null){
                    que.add(temp_p.right);
                    que.add(temp_q.right);
                }
                else if((temp_p.right != null && temp_q.right == null) || (temp_p.right == null && temp_q.right != null))
                    return false;

                    
            }
        }

        return true;
    }
}