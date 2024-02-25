class Solution {
    public boolean validMountainArray(int[] arr) {
        boolean asc = false;
        boolean des = false;
    
        
        for(int i = 1; i<arr.length; i++){
            if(!des && arr[i-1] < arr[i]){
                asc = true;
            }
            else if(asc && arr[i-1] > arr[i]){
                des = true;
            }
            else
                return false;
        }
        
        return asc && des ? true : false;
    }
}