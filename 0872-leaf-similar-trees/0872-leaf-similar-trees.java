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

    LinkedList<Integer> root1_list = null;
    LinkedList<Integer> root2_list = null;

    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        root1_list = new LinkedList<Integer>();
        root2_list = new LinkedList<Integer>();
        
        findLeaf(root1, root1_list);
        findLeaf(root2, root2_list);
        
        if(root1_list.size() != root2_list.size())
            return false;

        for(int i = 0; i<root1_list.size(); i++){
            if(root1_list.get(i) != root2_list.get(i))
                return false;
        }

        return true;
    }

    public void findLeaf(TreeNode root, LinkedList<Integer> root_list){
        if(root.left == null && root.right == null){
            root_list.add(root.val);
        }
        
        if(root.left != null)
            findLeaf(root.left, root_list);
            
        if(root.right != null)
            findLeaf(root.right, root_list);
    }
}