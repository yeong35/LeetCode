public class Solution {
    int max = 0;
    
    public int diameterOfBinaryTree(TreeNode root) {
        return depth(root.left) + depth(root.right);
    }
    
    private int depth(TreeNode root) {
        if(root == null)
            return 0;
        return 1 + Math.max(depth(root.left), depth(root.right));
    }
}