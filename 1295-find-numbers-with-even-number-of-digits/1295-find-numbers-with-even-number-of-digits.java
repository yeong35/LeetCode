class Solution {
    public int findNumbers(int[] nums) {
        String temp = null;
        int cnt = 0;
        int answer = 0;

        for(int n : nums){
            while(n>0){
                n = n/10;
                cnt++;
            }

            if(cnt%2==0)
                answer++;

            cnt=0;
        }

        return answer;
    }
}