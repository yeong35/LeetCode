class Solution {
    public int findJudge(int n, int[][] trust) {
        int[] cnt = new int[n+1];
        boolean[] check = new boolean[n+1];
        int index = 0;

        for(int i = 0; i<trust.length; i++){
            check[trust[i][0]] = true;
            for(int j = 1; j<trust[0].length; j++){
                index = trust[i][j];
                cnt[index]++; 
            }
        }

        for(int i = 1; i<=n; i++){
            if(!check[i] && cnt[i]==n-1) 
                return i;
        }

        return -1;

    }
}