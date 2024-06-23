class Solution {
    public int dominantIndex(int[] nums) {

        int max = -1;
        int index = -1;

        for(int i = 0; i<nums.length; i++){
            if(max < nums[i])
                max = nums[i];
        }

        for(int i = 0; i<nums.length; i++){
            if(max != nums[i] && max < nums[i]*2)
                return -1;
            
            if(max == nums[i])
                index = i;
        }

        return index;

    }
}