class Solution {
    public void rotate(int[] nums, int k) {
        int[] result = nums.clone();

        for(int i = 0; i<nums.length; i++){
            nums[(i+k)%nums.length] = result[i];
        }

    }
}