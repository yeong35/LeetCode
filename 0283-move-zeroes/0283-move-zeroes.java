class Solution {
    public void moveZeroes(int[] nums) {
        
        int write = 0;
        int temp;

        for(int read = 0; read<nums.length; read++){
            if(nums[read] != 0){
                temp = nums[write];
                nums[write] = nums[read];
                nums[read] = temp;
                write++;
            }
        }

    }
}