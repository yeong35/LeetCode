class Solution {
    public int minDifference(int[] nums) {

        if (nums.length < 5)
            return 0;

        Arrays.sort(nums);
        int sum = 0;
        int head = 0;
        int tail = nums.length - 1;

        for (int i = 0; i < nums.length; i++)
            sum += nums[i];

        for (int i = 0; i < 3; i++) {
            if (head >= tail)
                return 0;
            
            if (Math.abs(nums[head] - sum / (tail - head + 1)) > Math.abs(nums[tail] - sum / (tail - head + 1))) {
                sum -= nums[head];
                head++;
            } 
            else {
                sum -= nums[tail];
                tail--;
            }

        }
        return nums[tail] - nums[head];
    }
}
