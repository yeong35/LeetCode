class Solution {
    public int numIdenticalPairs(int[] nums) {
        int[] cnt = new int[101];
        int result = 0;
        
        for(int i = 0; i<nums.length; i++){
            cnt[nums[i]]++;
        }

        for(int i = 100; i>=0; i--){
            if(cnt[i]<2)
                continue;

            result += cnt[i]*(cnt[i]-1)/2;
        }

        return result;


    }
}