class Solution {
    public int[] twoSum(int[] numbers, int target) {

        int[] result = new int[2];
        int key;
        int secondIndex;

        for(int i = 0; i<numbers.length; i++){
            result[0] = i+1;
            key = target - numbers[i];

            secondIndex = binarySearch(numbers, i+1, numbers.length-1, key);

            if(secondIndex != -1){
                result[1] = secondIndex+1;
                break;
            }
            
        }

        return result;
    }

    public static int binarySearch(int[] numbers, int low, int high, int key){
        
        if(high >= low){
            int mid = low + (high-low)/2;

            if(numbers[mid] == key)
                return mid;
            else if(numbers[mid] > key)
                return binarySearch(numbers, low, mid - 1, key);
            else
                return binarySearch(numbers, mid + 1, high, key);
        }

        return -1;
    }
}