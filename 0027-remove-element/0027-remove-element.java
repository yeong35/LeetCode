class Solution {
    public int removeElement(int[] nums, int val) {
        int cnt = nums.length;
        for(int i = nums.length-1; i>-1; i--){
            if(nums[i] == val){
                for(int j = i; j<nums.length-1; j++)
                    nums[j] = nums[j+1];
                cnt--;
            }
        }
        return cnt;
    }
}