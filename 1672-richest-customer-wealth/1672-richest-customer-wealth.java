class Solution {
    public int maximumWealth(int[][] accounts) {
        int max = 0;

        for(int i = 0; i < accounts.length; i++){
            for(int j = 1; j<accounts[0].length; j++){
                accounts[i][j] += accounts[i][j-1];
            }
        }

        for(int i = 0; i<accounts.length; i++)
            max = accounts[i][accounts[0].length-1] > max ? accounts[i][accounts[0].length-1] : max;

        return max;
    }
}