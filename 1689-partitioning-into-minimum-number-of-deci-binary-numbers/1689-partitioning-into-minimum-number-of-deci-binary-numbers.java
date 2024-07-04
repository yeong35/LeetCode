class Solution {
    public int minPartitions(String n) {
        int max = -1;

        for(int i = 0; i<n.length(); i++){
            max = max > n.charAt(i)-'0' ? max : n.charAt(i)-'0';
        }

        return max;
    
    }
}