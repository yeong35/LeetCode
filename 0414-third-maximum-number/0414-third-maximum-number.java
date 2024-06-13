class Solution {
    public int thirdMax(int[] nums) {
        HashSet<Integer> set = new HashSet<>();

        for(int i = 0; i<nums.length; i++){
            set.add(nums[i]);
        }

        Integer[] arr = set.toArray(new Integer[0]);

        Arrays.sort(arr, Collections.reverseOrder());

        if(arr.length > 2)
            return arr[2];
        else
            return arr[0];
    }
}