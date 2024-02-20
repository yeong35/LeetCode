class Solution {
    public void duplicateZeros(int[] arr) {
        for(int i = 0; i<arr.length; i++){
            if(arr[i] == 0){
                arr = rightShift(arr, i);
                i++;
            }
        }
    }

    public int[] rightShift(int[] arr, int idx){
        if(idx < arr.length){
            for(int i = arr.length-1; i>idx; i--){
                arr[i] = arr[i-1];
            }
        }

        return arr;
    }
}