class Solution {
    public int removeElement(int[] nums, int val) {
        int temp;
        int write = 0;
        int k = 0;

        for(int read = 0; read<nums.length; read++){
            if(nums[read] != val){
                temp = nums[write];
                nums[write] = nums[read];
                nums[read] = temp;
                write++;
                k++;
            }
        }

        return k;
    }
}