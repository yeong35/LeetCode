class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        
        for(int i = 0; i<flowerbed.length; i++){
            if(i==0){
                if(flowerbed[i]==0 && (flowerbed.length==1 || flowerbed[i+1]==0)){
                    System.out.println("wjrldy");
                    n--;
                    flowerbed[i]=1;
                }
            }
            else if(i==flowerbed.length-1){
                if(flowerbed[i]==0 && flowerbed[i-1]==0){
                    n--;
                    flowerbed[i]=1;
                }
            }
            else if(flowerbed[i-1] == 0 && flowerbed[i] == 0 && flowerbed[i+1] == 0){
                n--;
                flowerbed[i]=1;
            }
        }
        System.out.println(n);
        if(n<=0)
            return true;
        else
            return false;
    }
}