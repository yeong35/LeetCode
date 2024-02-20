class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int cnt = 0; 
        int answer = 0;
        for(int i = 0; i<nums.length; i++){
            if(nums[i]==1)
                cnt++;
            else
                cnt=0;
            answer = cnt > answer ? cnt : answer;
        }
        
        return answer;
    }
}