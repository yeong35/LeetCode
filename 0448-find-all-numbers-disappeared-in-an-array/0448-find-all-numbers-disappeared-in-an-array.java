class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        LinkedList<Integer> result = new LinkedList<>();

        int[] counters = new int[nums.length+1];

        for(int i = 0; i<nums.length; i++){
            counters[nums[i]]++; 
        }

        for(int i = 1; i<counters.length; i++)
            if(counters[i] == 0)
                result.add(i);

        return result;
    }
}