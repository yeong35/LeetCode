class Solution {
    public double findMaxAverage(int[] nums, int k) {
        
        int cnt = 0;
        double sum = 0;
        double result = Integer.MIN_VALUE;

        for(int i = 0; i<nums.length; i++){
            if(cnt<k){
                sum+=nums[i];
                cnt++;
            }
            else{
                sum-=nums[i-k];
                sum+=nums[i];
            }
            System.out.println(result+" "+sum/k);
            result = Math.max(result, sum/k);
        }

        return result;
    }
}